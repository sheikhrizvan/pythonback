import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title,year,author,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows



def update(id,title, author, isbn, year):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, isbn=?, year=? WHERE id=?",(title,author,isbn,year, id))
    conn.commit()
    conn.close()


def search(title="", year="", author="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR year=? OR author=? OR isbn=?",(title, year, author, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows
    

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()








connect()

#insert("the earth","arhaan sheikh",2020,54545455454545)
#pdate(1,"The Earth","Dua Sheikh",2020,454545445)

#print(search(author="Rizvan Sheikh"))

