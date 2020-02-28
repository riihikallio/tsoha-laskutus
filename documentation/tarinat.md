# Käyttäjien tarinoita

Roolissa | Haluan | Jotta | Toteutettu
--- | --- | --- | ---
Käyttäjä | Luoda tunnuksen  | | X
Käyttäjä | Kirjautua sisään  | | X
Käyttäjä | Nähdä asiakkaat  | | X
Käyttäjä | Lisätä asiakkaan  | | X
Käyttäjä | Muokata asiakasta  | | X
Käyttäjä | Poistaa asiakkaan  | | X
Käyttäjä | Nähdä tuotteet  | | X
Käyttäjä | Lisätä tuotteen  | | X
Käyttäjä | Muokata tuotetta  | | X
Käyttäjä | Poistaa tuotteen  | | X
Käyttäjä | Nähdä luettelon laskuista  | | X
Käyttäjä | Nähdä laskun riveineen  | | X
Käyttäjä | Lisätä laskun  | | X
Käyttäjä | Muokata laskua  | | X
Käyttäjä | Poistaa laskun  | | X
Ylläpitäjä | Rajoittaa käyttäjät omiin laskuihinsa | Väärinkäytösten välttämiseksi | X
Käyttäjä | Nähdä laskun rivit  | | X
Käyttäjä | Lisätä laskuun rivejä  | | X
Käyttäjä | Muokata laskun rivejä  | | X
Käyttäjä | Poistaa laskun rivin  | | X
Esimies | Nähdä tuoteryhmien myyntiraportin  | | X
Esimies | Nähdä asiakkaiden myyntiraportin  | | X

## Vastaavat SQL-kyselyt

### Kirjautua sisään

```sql
SELECT account.date_created AS account_date_created,
    account.date_modified AS account_date_modified,
    account.id AS account_id,
    account.name AS account_name,
    account.username AS account_username,
    account.password AS account_password
FROM account
WHERE account.username = ? AND account.password = ?
LIMIT ? OFFSET ?
```

### Luoda tunnuksen

```sql
INSERT INTO account (date_created, date_modified, name, username, password)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

### Nähdä asiakkaat

```sql
SELECT customer.date_created AS customer_date_created,
    customer.date_modified AS customer_date_modified,
    customer.number AS customer_number,
    customer.name AS customer_name,
    customer.address AS customer_address
FROM customer
LIMIT ? OFFSET ?
 ```

### Lisätä asiakkaan

```sql
INSERT INTO customer (date_created, date_modified, name, address)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```

### Muokata asiakasta

```sql
UPDATE customer SET date_modified=CURRENT_TIMESTAMP, address=?
WHERE customer.number = ?
```

### Poistaa asiakkaan

```sql
DELETE FROM customer WHERE customer.number = ?
```

### Nähdä tuotteet

```sql
SELECT product.date_created AS product_date_created,
    product.date_modified AS product_date_modified,
    product.number AS product_number,
    product.name AS product_name,
    product.unit AS product_unit,
    product.price AS product_price,
    product.category AS product_category
FROM product
LIMIT ? OFFSET ?
```

### Lisätä tuotteen

```sql
INSERT INTO product (date_created, date_modified, name, unit, price, category)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, )
```

### Muokata tuotetta

```sql
UPDATE product SET date_modified=CURRENT_TIMESTAMP, category=?
WHERE product.number = ?
```

### Poistaa tuotteen

```sql
DELETE FROM product WHERE product.number = ?
```

### Nähdä luettelon laskuista

```sql
SELECT invoice.date_created AS invoice_date_created,
    invoice.date_modified AS invoice_date_modified,
    invoice.number AS invoice_number,
    invoice.customer_num AS invoice_customer_num,
    invoice.account_id AS invoice_account_id
FROM invoice
WHERE ? = invoice.account_id
LIMIT ? OFFSET ?
```

### Nähdä laskun riveineen

```sql
SELECT invoice.date_created AS invoice_date_created,
    invoice.date_modified AS invoice_date_modified,
    invoice.number AS invoice_number,
    invoice.customer_num AS invoice_customer_num,
    invoice.account_id AS invoice_account_id
FROM invoice
WHERE ? = invoice.account_id

row.date_created AS row_date_created,
    row.date_modified AS row_date_modified,
    row.id AS row_id,
    row.product_num AS row_product_num,
    row.qty AS row_qty,
    row.invoice_num AS row_invoice_num
FROM row
WHERE ? = row.invoice_num

SELECT product.date_created AS product_date_created,
    product.date_modified AS product_date_modified,
    product.number AS product_number,
    product.name AS product_name,
    product.unit AS product_unit,
    product.price AS product_price,
    product.category AS product_category
FROM product
WHERE product.number = ?

SELECT customer.date_created AS customer_date_created,
    customer.date_modified AS customer_date_modified,
    customer.number AS customer_number,
    customer.name AS customer_name,
    customer.address AS customer_address
FROM customer
WHERE customer.number = ?
```

### Lisätä laskun ja sen rivit

```sql
INSERT INTO invoice (date_created, date_modified, customer_num, account_id)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
INSERT INTO row (date_created, date_modified, product_num, qty, invoice_num)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

### Muokata laskua

Muokkauksen yhteydessä laskun rivit poistetaan ja luodaan uudelleen

```sql
UPDATE invoice SET date_modified=CURRENT_TIMESTAMP, customer_num=?, account_id=?
WHERE invoice.number = ?

DELETE FROM row WHERE row.id = ?

INSERT INTO row (date_created, date_modified, product_num, qty, invoice_num)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

### Poistaa laskun

```sql
DELETE FROM row WHERE row.id = ?

DELETE FROM invoice WHERE invoice.number = ?
```

### Rajoittaa käyttäjät omiin laskuihinsa

Tämä tapahtuu ohjelmallisesti. Aina laskuja käsiteltäessa tarkistetaan, onko käyttäjä laskun luoja.

### Nähdä laskun rivit

### Lisätä laskuun rivejä

### Muokata laskun rivejä

### Poistaa laskun rivin

Nämä tapahtuvat laskua muokatessa

### Nähdä tuoteryhmien myyntiraportin

```sql
SELECT Product.category,
    Account.name,
    SUM(Product.price*Row.qty) as Total
FROM Product
JOIN Row ON Product.number = Row.product_num
JOIN Invoice ON Invoice.number = Row.invoice_num
JOIN Account ON Account.id = Invoice.account_id
GROUP BY Product.category, Account.id
ORDER BY Product.category, Account.username
```

### Nähdä asiakkaiden myyntiraportin

```sql
SELECT Customer.name,
    Product.category,
    SUM(Product.price*Row.qty) as Total
FROM Customer
JOIN Invoice ON Invoice.customer_num = Customer.number
JOIN Row ON Row.invoice_num = Invoice.number
JOIN Product ON Product.number = Row.product_num
GROUP BY Customer.name, Product.category
ORDER BY Customer.name, Product.category
```
