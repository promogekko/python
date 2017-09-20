import sqlite3

db = sqlite3.connect(r'/home/hme/simplon/gekko/db/Chinook_Sqlite.sqlite')
#print(db)

cursor = db.cursor()
try:
    cursor.execute('''
    CREATE TABLE x (a INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, b TEXT not null unique)
                   ''')
except sqlite3.OperationalError:
    pass

try:
    cursor.execute('''
    CREATE TABLE y (c INTEGER NOT NULL, d TEXT not null unique)
                   ''')
except sqlite3.OperationalError:
    pass

try:
    cursor.execute('''
    CREATE TABLE z (a INTEGER NOT NULL, e TEXT not null unique)
                   ''')
except sqlite3.OperationalError:
    pass


name1 = 'alice'
name2 = 'bob'
name3 = 'charlie'

# Insert b 1
cursor.execute('''INSERT INTO x(b) VALUES(?)''', (name1,))
print('First name inserted')

# Insert b 2
cursor.execute('''INSERT INTO x(b) VALUES(?)''', (name2,))
print('Second name inserted')

# Insert b 3
cursor.execute('''INSERT INTO x(b) VALUES(?)''', (name3,))
print('Third name inserted')

value1 = '3.1415'
value2 = '2.74'
value3 = '1.61'

# Insert d 1
cursor.execute('''INSERT INTO y(c,d) VALUES(?,?)''', ("1",value1))
print('First value inserted')

# Insert d 2
cursor.execute('''INSERT INTO y(c,d) VALUES(?,?)''', ("1",value2))
print('Second value inserted')

# Insert d 3
cursor.execute('''INSERT INTO y(c,d) VALUES(?,?)''', ("2",value3))
print('Third value inserted')


value1 = '100'
value2 = '150'
value3 = '300'
value4 = '900'

# Insert d 1
cursor.execute('''INSERT INTO z(a,e) VALUES(?,?)''', ("1",value1))
print('First value inserted')

# Insert d 2
cursor.execute('''INSERT INTO z(a,e) VALUES(?,?)''', ("1",value2))
print('Second value inserted')

# Insert d 3
cursor.execute('''INSERT INTO z(a,e) VALUES(?,?)''', ("3",value3))
print('Third value inserted')

# Insert d 3
cursor.execute('''INSERT INTO z(a,e) VALUES(?,?)''', ("9",value4))
print('Fourth value inserted')


db.commit()