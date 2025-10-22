-- Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO Customers (customer_id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

-- Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50)
);

INSERT INTO Orders (order_id, customer_id, product) VALUES
(101, 1, 'Laptop'),
(102, 2, 'Phone'),
(103, 2, 'Tablet'),
(104, 4, 'Monitor');  -- notice: customer_id = 4 does not exist in Customers

-- INNER JOIN, only rows where value of common row in BOTH tables
SELECT c.customer_id, c.name, o.product
FROM Customers c INNER JOIN Orders o
ON c.customer_id = o.customer_id;

-- LEFT JOIN, joins all rows in left column, 
-- will have NULL in right table's column if value not present
SELECT c.customer_id, c.name, o.product
FROM Customers c LEFT JOIN Orders o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN, joins all rows in left column, 
-- will have NULL in LEFT table's column if value not present
SELECT c.customer_id, c.name, o.product
FROM Customers c RIGHT JOIN Orders o
ON c.customer_id = o.customer_id;

-- OUTER JOIN, All rows from both tables w.r.t matching columns
-- Unmatched rows show NULLs on one side.
SELECT c.customer_id, c.name, o.product
FROM Customers c FULL OUTER JOIN Orders o
ON c.customer_id = o.customer_id;