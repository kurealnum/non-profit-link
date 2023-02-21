#if i accidentally commit this, its legit just at test file
#for doing stuff with sqlite

import sqlite3

x = "Bob"
y = "Joe"

#connecting to the database
#CHANGE THIS TO YOUR OWN PATH
conn = sqlite3.connect('C:\Code\Python\AdvancedProjects\FlaskWebApp\database\database.db')
conn.execute('CREATE TABLE names__ (first_name TEXT, last_name TEXT)')
conn.execute("INSERT INTO names__ (first_name, last_name) VALUES (?,?)", (x, y))
conn.commit()
conn.close()