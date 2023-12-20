import sqlite3
sqlconn = sqlite3.connect('hotel.db')
cur = sqlconn.cursor()
print("Welcome to Hotel Management System\nConnected to Database")
create_tab = "CREATE TABLE HOTEL(ROOM_NO INT, NAME VARCHAR(40), PAYMENT INT, CHECK_IN DATE, CHECK_OUT DATE)"
try:
    cur.execute(create_tab)
    print("Table created successfully")
except:
    print("Error creating the table.The table might already exist")

# Data Entry
def entry(room : int, name : str, payment : int, check_in : str, check_out : str):
    cur.execute("INSERT INTO HOTEL VALUES(?,?,?,?,?)",(room,name,payment,check_in,check_out))
    sqlconn.commit()
    print("Data Entered Successfully")

# Data Deletion
def delete(room : int):
    cur.execute("DELETE FROM HOTEL WHERE ROOM_NO = ?",(room,))
    sqlconn.commit()
    print("Data Deleted Successfully")

# Data Updation
def update(room : int, name : str, payment : int, check_in : str, check_out : str):
    cur.execute("UPDATE HOTEL SET NAME = ?, PAYMENT = ?, CHECK_IN = ?, CHECK_OUT = ? WHERE ROOM_NO = ?",(name,payment,check_in,check_out,room))
    sqlconn.commit()
    print("Data Updated Successfully")

# Data Display
def display():
    cur.execute("SELECT * FROM HOTEL")
    l = cur.fetchall()
    if len(l) == 0:
        print("No data to display")
    else:
        print(l)

# Data Search
def search(room : int):
    cur.execute("SELECT * FROM HOTEL WHERE ROOM_NO = ?",(room,))
    l = cur.fetchall()
    if len(l) == 0:
        print("No data found")
    else:
        print(l)

q = input("What you want to do?\na = enter data\nd = delete data\nu = update data\ns = search data\ndi = display data\nq = exit database system\n")
while q != "q":
    if q == "a":
        entry(int(input("Enter Room Number: ")),input("Enter Name: "),int(input("Enter Payment: ")),input("Enter Check In Date(dd-mm-yyyy): "),input("Enter Check Out Date(dd-mm-yyyy): "))
        print("Existing data:")
        cur.execute("SELECT * FROM HOTEL")
        print(cur.fetchall())
    elif q == "d":
        delete(int(input("Enter Room Number: ")))
        print("Existing data:")
        cur.execute("SELECT * FROM HOTEL")
        print(cur.fetchall())
    elif q == "u":
        update(int(input("Enter Room Number: ")),input("Enter Name: "),int(input("Enter Payment: ")),input("Enter Check In Date(dd-mm-yyyy): "),input("Enter Check Out Date(dd-mm-yyyy): "))
        print("Existing data:")
        cur.execute("SELECT * FROM HOTEL")
        print(cur.fetchall())
    elif q == "s":
        search(int(input("Enter Room Number: ")))
    elif q == "di":
        display()
    else:
        print("Please enter a valid operation")
    q = input("What you want to do?\na = enter data\nd = delete data\nu = update data\ns = search data\ndi = display data\nq = exit database system\n")
    sqlconn.commit()
print("Thank you for using Hotel Management System")
sqlconn.close()