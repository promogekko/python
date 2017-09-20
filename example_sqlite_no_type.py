import sqlite3

db = sqlite3.connect(r'/home/hme/simplon/gekko/db/Chinook_Sqlite.sqlite')
#print(db)

cursor = db.cursor()
try:
    cursor.execute('''
    CREATE TABLE x (a , b)
                   ''')
except sqlite3.OperationalError:
    pass

try:
    cursor.execute('''
    CREATE TABLE y (c, d)
                   ''')
except sqlite3.OperationalError:
    pass

try:
    cursor.execute('''
    CREATE TABLE z (a ,e)
                   ''')
except sqlite3.OperationalError:
    pass

name1 = 'alice'
name2 = 'bob'
name3 = 'charlie'

# Insert b 1
cursor.execute('''INSERT INTO x(a,b) VALUES(?,?)''', (1,name1))
print('First name inserted')

# Insert b 2
cursor.execute('''INSERT INTO x(a,b) VALUES(?,?)''', (2,name2))
print('Second name inserted')

# Insert b 3
cursor.execute('''INSERT INTO x(a,b) VALUES(?,?)''', (3,name3))
print('Third name inserted')

value1 = 3.1415
value2 = 2.74
value3 = 1.61

# Insert d 1
cursor.execute('''INSERT INTO y (c,d) VALUES(?,?)''', (1,value1))
print('First value inserted')

# Insert d 2
cursor.execute('''INSERT INTO y(c,d) VALUES(?,?)''', (1,value2))
print('Second value inserted')

# Insert d 3
cursor.execute('''INSERT INTO y(c,d) VALUES(?,?)''', (2,value3))
print('Third value inserted')

value1 = 100
value2 = 150
value3 = 300
value4 = 900
val1= 1
val2= 1
val3 = 3
val4 = 9

z_value = [(val1, value1),
           (val2,value2),
           (val3,value3),
           (val4,value4)
          ]

cursor.executemany('''INSERT INTO z(a,e) VALUES(?,?)''', z_value)


db.commit()
db.close()