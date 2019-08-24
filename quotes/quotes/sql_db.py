import sqlite3

# if 'myquotes.db' doesn't exist - it will create this file, otherwise - connect
connection = sqlite3.connect('myquotes.db')
cursor = connection.cursor()

# lines below are commented out because the table once once created and running the code afterwards will cause
# an error, cause ... you know - it's been already created, wy do we need to create it one more time

# cursor.execute("""create table quotes_db(
#                     title text,
#                     author text,
#                     tag text
#                     )""")

# adding values manually to our table
cursor.execute("""insert into quotes_db values ('I like apples', 'sachsene', 'food')""")
connection.commit()
connection.close()