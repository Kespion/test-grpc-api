import sqlite3

# Connection to the database (the file will be created if it does not exist)
conn = sqlite3.connect('devices.db')

# Creating the table
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        os TEXT NOT NULL,
        version TEXT NOT NULL,
        wifi BOOLEAN NOT NULL,
        bluetooth BOOLEAN NOT NULL
    )
''')

# Saving changes
conn.commit()

# Closing the connection
conn.close()
