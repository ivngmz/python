import sqlite3


class Database:
    
    def __init__(self,db):
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY,title text, author text, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()

    def insert(self,title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM books")
        rows=cur.fetchall()
        conn.close()
        return rows
        
    def search(self,title="",author="",year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(self,id,title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        conn.commit()
        conn.close()