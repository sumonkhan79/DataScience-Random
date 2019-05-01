import sqlite3
conn = sqlite3.connect('/Users/sumon/sql2.db')
print(conn)
cur = conn.cursor()
print("cursor is now pointed to the database")
cur.execute('drop table if exists Counts')
cur.execute('create table Counts(email TEXT,count INTEGER)')
print('table is created now')
cur.execute('select * from Counts')
fname = input('enter the file name:')
if (len(fname)<1): fname = '/Users/sumon/mbox-short.txt'
fh = open(fname)
#print(fh)
for line in fh:
    if not line.startswith('From: '): continue
    pieces=line.split()
    #print(pieces)
    email=pieces[1]
    #print(email)
    cur.execute('select count from Counts where email =?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into Counts values (?,1)',(email,))
    else:
        cur.execute('update Counts set count=count+1 where email =?',(email,))
        conn.commit()
sqlstr = 'select email, count from Counts order by 2'
for row in cur.execute(sqlstr):
    print (str(row[0]),row[1])
cur.close()

