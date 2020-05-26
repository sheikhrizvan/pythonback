import sqlite3

class Backend_Operation():
    def __init__(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()


    def insert(self,title,year,author,isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
        conn.commit()
        conn.close()


    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows



    def update(self,id,title, author, isbn, year):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, isbn=?, year=? WHERE id=?",(title,author,isbn,year, id))
        conn.commit()
        conn.close()


    def search(self,title="", year="", author="", isbn=""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR year=? OR author=? OR isbn=?",(title, year, author, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows
        

    def delete(self,id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()

