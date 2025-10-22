-- create table
CREATE TABLE product (
	prodnames VARCHAR,
	prodqty INTEGER,
	prodprice INTEGER
);

-- insert value into table
INSERT INTO product (prodnames, prodqty, prodprice)
				 -- (column 1, column 2, column 3)
VALUES ('shoes', 5, 65), ('pants', 5, 30);
	-- (Seperate values in each row with brackets, 
	-- must match number of entries in top line)

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

-- add column
ALTER TABLE product
ADD COLUMN discount VARCHAR(2);

-- change column data type
ALTER TABLE product
ALTER COLUMN discount TYPE INTEGER
USING discount::integer; -- casting

-- altering data with conditions/cases
UPDATE product
SET discount = CASE 
				WHEN prodprice < 40 
				OR prodprice > 100 THEN 'Y'
				ELSE 'N'
				END;

-- create new table for linking 
-- ...
CREATE TABLE supplier (
	name VARCHAR(255)
	supplierid SERIAL PRIMARY KEY; --makes it list like
	CONSTRAINT fkprod
			FOREIGN KEY(supplierid) --column in this table
				REFERENCES "product"(prodnames) 
				-- references (prodnames) column in other table "product"
);

UPDATE supplier
SET supplierid = 2
WHERE name = 'Nike';

UPDATE supplier
SET supplierid = 1
WHERE name = 'Levis';

-- update default table
ALTER TABLE product
ADD COLUMN supplierid INTEGER; -- same name

UPDATE product
SET supplierid = 2
WHERE prodnames = 'Jeans';


