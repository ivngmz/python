import psycopg2

# Use precompiled python libraries
# https://www.lfd.uci.edu/~gohlke/pythonlibs/
# Descargo: https://download.lfd.uci.edu/pythonlibs/x6hvwk7i/psycopg2-2.9.2-cp39-cp39-win_amd64.whl

# docker run -d     --name some-postgres     -e POSTGRES_PASSWORD=Password -p 5432:5432     -e PGDATA=/var/lib/postgresql/data/pgdata     -v /custom/mount:/var/lib/postgresql/data     postgres
# docker exec -it 02ee0b8bed45 /bin/bash
# postgres psql -U postgres
# create database store;
# create user developMan with encrypted password 'Password';
# grant all privileges on database store to developMan;


def create_table():
    conn=psycopg2.connect("dbname='store' user='postgres' password='Zaragoza2020' host='192.168.0.245' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='store' user='postgres' password='Zaragoza2020' host='192.168.0.245' port='5432'")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='store' user='postgres' password='Zaragoza2020' host='192.168.0.245' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='store' user='postgres' password='Zaragoza2020' host='192.168.0.245' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='store' user='postgres' password='Zaragoza2020' host='192.168.0.245' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

def view2():
    conn=psycopg2.connect("dbname='store' user='postgres' password='Zaragoza2020' host='192.168.0.245' port='5432'")
    cur=conn.cursor()
    cur.execute("select count(item) from store where item = 'Beer'")
    rows=cur.fetchall()
    conn.close()
    return rows



# create_table()
# insert("Bacon",10,15)
# insert("Beer",10,5)
# insert("Wine Glass",10,5)

# print(view())

delete("Beer")

print(view())

print(view2())

# update(13,3,"Beer Cup")

# print(view())