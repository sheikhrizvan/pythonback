import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()


def inser_data(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, qty, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
# in above line " , " after item is important otherwise throws error
    conn.commit()
    conn.close()

def update(qty, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET qty=?, price=? WHERE item=?", (qty, price, item))
    conn.commit()
    conn.close()


print(view())
update(20, 12.5, "wine glass")
print(view())
