## Based on the Coursera Specialization: PostgreSQL for Everybody Specialization by University of Michigan

#### SQL (Structured Query Language): used for (CRUD)
- Create/Insert data
- Read/Select data
- Update data
- Delete data

#### Relations (Tables), Tuples (Rows), Attributes (Columns)
A relation is a set of tuples (or data points/objects) with the same attributes!

### SQL Architecture
User database Interacts with pgCLI or the pgAdmin 
- on pgCLI we run (linux, but similar for windows): 
- - $ psql -U postgres
- - postgres=#
- - postgres=# CREATE USER <user> WITH PASSWORD <password>
- - CREATE TABLE users(
        name VARCHAR(128),
        email VARCHAR(128)
    );
- - 