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