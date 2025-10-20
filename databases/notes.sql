-- create table
CREATE TABLE product (
	prodnames VARCHAR,
	prodqty INTEGER,
	prodprice INTEGER
);

-- insert value into table
INSERT INTO product (prodnames, prodqty, prodprice)
VALUES ('shoes', 5, 65), ('pants', 5, 30);

-- view entire table
SELECT *
FROM product;

-- view certain columns
SELECT prodnames
FROM product;

-- view rows of certain columns under certain conditions
SELECT prodnames
FROM product
WHERE prodprice > 45;


-- update values (on condition)
UPDATE product
SET prodprice = prodprice - 10
WHERE prodprice > 40;

-- delete values (on condition)
DELETE FROM product
WHERE prodnames = 'wrong';