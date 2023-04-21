#DEFAULT COMMAND: python update_db.py database.db schema.sql
#(as long as you're in the database folder)

#we're gonna use argv to be fancy and have a CLA
import sys

#db file is under .gitignore
import sqlite3

def main():
    
    if len(sys.argv) != 3:
        print("Usage: python update_db.py PATH_TO_DB PATH_TO_SCHEMA\n(If the file is in the same dir, just provide the file name)")
        return

    #connecting to the database
    conn = sqlite3.connect(sys.argv[1], check_same_thread=False)

    cursor = conn.cursor()

    with open(sys.argv[2]) as f:
        cursor.executescript(f.read())

    conn.commit()
    cursor.close()
    conn.close()

main()
