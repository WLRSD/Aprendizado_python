import sqlite3

def create_db():
    connection = sqlite3.connect('exercises.db')  
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_id INTEGER,
        name TEXT,
        code_path TEXT,
        markdown_path TEXT,
        completed INTEGER,
        FOREIGN KEY (level_id) REFERENCES levels (id)
    );
    ''')

    connection.commit() 
    connection.close() 

create_db()
