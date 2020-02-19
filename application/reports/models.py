from application import db

def sales_by_category():
  stmt = "SELECT Product.category, Account.username, SUM(Product.price*Row.qty) FROM Product"
  stmt += " LEFT JOIN Row ON Product.number = Row.product_num"
  stmt += " LEFT JOIN Invoice ON Invoice.number = Row.invoice_num"
  stmt += " LEFT JOIN Account ON Account.id = Invoice.account_id"
  stmt += " GROUP BY Product.category, Account.id"

  res = db.engine.execute(stmt)
  
  total = 0
  grand = 0
  prev = None
  result = []
  
  for row in res:
    if prev==None:
      prev = row[0]
      result.append(row)
    elif not prev == row[0]:
      result.append(["", prev + " total:", total])
      total = 0
      prev = row[0]
      result.append(row)
    else:
      result.append(["", row[1], row[2]])
    total += row[2]
    grand += row[2]

  result.append(["", prev + " total:", total])
  result.append(["Grand total:", "", grand])  
  return result


def sales_by_customer():
  stmt = "SELECT Customer.name, Product.category, SUM(Product.price*Row.qty) FROM Customer"
  stmt += " LEFT JOIN Invoice ON Invoice.customer_num = Customer.number"
  stmt += " LEFT JOIN Row ON Row.invoice_num = Invoice.number"
  stmt += " LEFT JOIN Product ON Product.number = Row.product_num"
  stmt += " GROUP BY Customer.name, Product.category"

  res = db.engine.execute(stmt)
  
  total = 0
  grand = 0
  prev = None
  result = []
  
  for row in res:
    if prev==None:
      prev = row[0]
      result.append(row)
    elif not prev == row[0]:
      result.append(["", prev + " total:", total])
      total = 0
      prev = row[0]
      result.append(row)
    else:
      result.append(["", row[1], row[2]])
    total += row[2]
    grand += row[2]

  result.append(["", prev + " total:", total])
  result.append(["Grand total:", "", grand])  
  return result