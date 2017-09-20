import sqlite3

db = sqlite3.connect(r'/home/hme/simplon/gekko/db/Chinook_Sqlite.sqlite')
#print(db)

# -- row factory
db.row_factory = sqlite3.Row

cursor = db.cursor()
cursor.execute('''SELECT a, b, c, d FROM x JOIN y''')
for row in cursor:
    #
    print('{0} : {1}, {2} {3}'.format(row['a'], row['b'], row['c'], row['d']))


#cursor.execute('''SELECT d, d*d as v FROM y''')
#for row in cursor:
#    #
#    print('{0} : {1}'.format(row['d'], row['v']))



#cursor.execute ('''SELECT c, d, c+d AS sum FROM y WHERE sum < 4.0''')
#for row in cursor:
#    #
#    print('{0} : {1} :  {2}'.format(row['c'], row['d'], row['sum']))

cursor.execute('''
        select title as album,
        group_concat(distinct genre.name) as genres
        from      track
             join genre using(genreid)
             join album using(albumid)
        group by title
        having count(distinct genre.name) > 1;
''')
for row in cursor:
    #
    print('{0} ==> {1}'.format(row['album'], row['genres']))







db.commit()
db.close()


