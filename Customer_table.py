import sqlite3 as sq

# The program for creating table with specified columns inside the database.
with sq.connect("mydb.db") as con:
    cur = con.cursor()

    cur.execute("""DROP TABLE IF EXISTS customer""")

    cur.execute("""CREATE TABLE IF NOT EXISTS customer(
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL, 
        lname TEXT NOT NULL, 
        address TEXT, 
        mobile TEXT NOT NULL)""")

    cur.execute('''INSERT INTO customer (fname, lname, address, mobile) VALUES
    ('Ana', 'Trujillo', 'Constitución 2222, México D.F.', '05 555 4729')''')
    cur.execute('''INSERT INTO customer (fname, lname, address, mobile) VALUES 
    ('Thomas', 'Hardy', 'Hanover Sq.120, London', '0171 555 7788')''')
    cur.execute('''INSERT INTO customer (fname, lname, address, mobile) VALUES 
    ('Christina', 'Berglund', 'Berguvsvagen  8, Stockholm, Sweden', '0921 12 34 65')''')
    cur.execute('''INSERT INTO customer (fname, lname, address, mobile) VALUES 
    ('Hanna', 'Moos', 'Forsterstr 57, Mannheim, Germany', '0621 08924')''')
    cur.execute('''INSERT INTO customer (fname, lname, address, mobile) VALUES
    ('Elizabeth', 'Lincoln', 'Hauptstr. 29, Bern, Switzerland', '0452 076545')''')
