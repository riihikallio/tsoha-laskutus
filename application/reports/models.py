from application import db

def tabulate(res):
  total = 0
  grand = 0
  prev = None
  result = []
  
  for row in res:
    amount = 0 if row[2]==None else row[2]
    if prev==None:  # First row
      prev = row[0]
      result.append([row[0], "", ""])
    elif not prev == row[0]:  # Subtotal
      result.append(["", "Total:", '{:.2f}€'.format(total)])
      total = 0
      prev = row[0]
      result.append([row[0], "", ""])
    result.append(["", row[1], '{:.2f}€'.format(amount)])
    total += amount
    grand += amount

  result.append(["", "Total:", '{:.2f}€'.format(total)])
  result.append(["Grand total:", "", '{:.2f}€'.format(grand)])  
  return result


def sales_by_category():
  stmt = "SELECT Product.category, Account.name, SUM(Product.price*Row.qty) as Total FROM Product"
  stmt += " LEFT JOIN Row ON Product.number = Row.product_num"
  stmt += " LEFT JOIN Invoice ON Invoice.number = Row.invoice_num"
  stmt += " LEFT JOIN Account ON Account.id = Invoice.account_id"
  stmt += " GROUP BY Product.category, Account.id"
  stmt += " HAVING Total > 0"
  stmt += " ORDER BY Product.category, Account.username"

  return tabulate(db.engine.execute(stmt))


def sales_by_customer():
  stmt = "SELECT Customer.name, Product.category, SUM(Product.price*Row.qty) as Total FROM Customer"
  stmt += " LEFT JOIN Invoice ON Invoice.customer_num = Customer.number"
  stmt += " LEFT JOIN Row ON Row.invoice_num = Invoice.number"
  stmt += " LEFT JOIN Product ON Product.number = Row.product_num"
  stmt += " GROUP BY Customer.name, Product.category"
  stmt += " HAVING Total > 0"
  stmt += " ORDER BY Customer.name, Product.category"

  return tabulate(db.engine.execute(stmt))