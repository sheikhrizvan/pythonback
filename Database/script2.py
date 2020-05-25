import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='Passw0rd' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert_data(item, qty, price):
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='Passw0rd' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, qty, price))
    conn.commit()
    conn.close()
    print("Data Saved Successfully..")


def view():
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='Passw0rd' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='Passw0rd' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
# in above line " , " after item is important otherwise throws error
    conn.commit()
    conn.close()


def update(qty, price, item):
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='Passw0rd' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET qty=%s, price=%s WHERE item=%s", (qty, price, item))
    conn.commit()
    conn.close()



while True:
    #Menu
    print("Welcome to AR Store.")
    print("Select Options ")
    print("1: Insert data")
    print("2: Update data")
    print("3: Show data")
    print("4: Delete data")
    opt = int(input("Enter Option: "))

    if opt == 1:
        item = input("Enter Item name: ")
        item = item.title()
        qty = int(input("Enter quantity: "))
        price = int(input("Enter price per item: "))
        insert_data(item, qty, price)

    elif opt == 2:
        item = input("Enter Item name to update: ")
        qty = int(input("Enter quantity to update: "))
        price = int(input("Enter price per item to update: "))
        update(qty, price, item)

    elif opt == 3:
        a = view()
        for item in a:
            print("product:", item[0], "Quantity: ",item[1], "price:", item[2])

    elif opt == 2:
        item = input("Enter Item name to Delete: ")

    else:
        print("Please select valid Option...")
