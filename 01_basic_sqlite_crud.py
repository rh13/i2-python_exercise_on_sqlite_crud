import sqlite3

db = sqlite3.connect('author.db')
author=db.cursor()

author.execute('''CREATE TABLE authors(id INTEGER PRIMARY KEY, username TEXT unique,
                       author_name TEXT)''')

author_list=(('1','almasud','Abdullah Al Masud'),('2','rimon','Rimon Ali'),('3','niloy','Niloy Roy'),('4','sourav','Sourav De Sharma'),('5','sathi','Sathi Rani Roy'))

author.executemany("""INSERT INTO authors(id,username,author_name)
              VALUES(?,?,?)""",author_list)

author.execute('''SELECT id, author_name FROM authors''')
for row in author:
    print('{0}-{1}'.format(row[0], row[1]))

db.commit()
db.close()
