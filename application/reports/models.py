from application import db


def tabulate(res):
    total = 0
    grand = 0
    prev = None
    result = []

    for row in res:
        if prev == None:  # First row
            prev = row[0]
            result.append([row[0], "", ""])
        elif not prev == row[0]:  # Subtotal
            result.append(["", "Total:", '{:.2f}€'.format(total)])
            total = 0
            prev = row[0]
            result.append([row[0], "", ""])
        result.append(["", row[1], '{:.2f}€'.format(row[2])])
        total += row[2]
        grand += row[2]

    result.append(["", "Total:", '{:.2f}€'.format(total)])
    result.append(["Grand total:", "", '{:.2f}€'.format(grand)])
    return result


def sales_by_category():
    stmt = "SELECT Product.category, Account.name, SUM(Product.price*Row.qty) as Total FROM Product"
    stmt += " JOIN Row ON Product.number = Row.product_num"
    stmt += " JOIN Invoice ON Invoice.number = Row.invoice_num"
    stmt += " JOIN Account ON Account.id = Invoice.account_id"
    stmt += " GROUP BY Product.category, Account.id"
    stmt += " ORDER BY Product.category, Account.username"

    return tabulate(db.engine.execute(stmt))


def sales_by_customer():
    stmt = "SELECT Customer.name, Product.category, SUM(Product.price*Row.qty) as Total FROM Customer"
    stmt += " JOIN Invoice ON Invoice.customer_num = Customer.number"
    stmt += " JOIN Row ON Row.invoice_num = Invoice.number"
    stmt += " JOIN Product ON Product.number = Row.product_num"
    stmt += " GROUP BY Customer.name, Product.category"
    stmt += " ORDER BY Customer.name, Product.category"

    return tabulate(db.engine.execute(stmt))
