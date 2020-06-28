import sqlite3

connection = sqlite3.connect('phonebook.db')
c = connection.cursor()

c.execute(
    '''CREATE TABLE IF NOT EXISTS PHONEBOOK
        ( PHONE INT PRIMARY KEY, \
          NAME TEXT, \
          EMAIL TEXT \
          )'''
)
connection.commit()


def printMenu():
    print("0. Retrieve a phone number.")
    print("1. Add an entry.")
    print("2. Retrieve all entries.")
    print("3. Delete entry.")
    print("4. Quit.\n")


def retrieveEntry():
    phone = input("Enter a phone number to look up: ")
    c.execute(' SELECT * FROM Phonebook WHERE phone = ' + phone)
    lookUp = c.fetchall()
    print("\n", lookUp, "\n")


def addEntry():
    name = input('Enter the name: ')
    phone = input('Enter the phone number: ')
    email = input('Enter the email address: ')
    c.execute("INSERT INTO PHONEBOOK (PHONE, NAME, EMAIL) VALUES(" + phone + ", '" + name + ", "+ email + "')");
    connection.commit()
    print("\n(%s,%s) has been added to the phonebook!\n" % (phone, name))

def deleteEntry():
    phone = input('Enter the phone number to be deleted: ')
    c.execute("DELETE FROM Phonebook WHERE phone = " + phone )
    connection.commit()
    # lookUp = c.fetchall()
    print('\n deleted the said contact = ' + phone)

def retrieveAll():
    c.execute('SELECT * FROM Phonebook')
    allData = c.fetchall()
    print("\n", allData, "\n")





# db = sqlite3.connect('contacts.db')
#
# cur = db.cursor()
# cur.execute('create table if not exists'\
#             + ' contacts(name text, phone text)')
# cur.execute('insert into contacts values(?, ?)',
#             ('abc', '1234'))
#
# numbers = [
#     ('abc',' 9801'),
#     ('bcd', '801290')
# ]
# cur.executemany('insert into contacts values(?,?)',
#                 numbers)
#
# cur.execute('select * from contacts')
# cts = cur.fetchall()
# print('contacts:',cts)
# while True:
#     contact = cur.fetchone()
#     if not contact:
#         break
#     name, number = contact
#     print('{}: {}'.format(name, number))
#
# db.commit()
# db.close()