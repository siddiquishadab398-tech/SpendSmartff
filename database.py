import sqlite3

def setup_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    
    # Create Users Table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    
    # Create Transactions Table
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                 id INTEGER PRIMARY KEY, 
                 user_id INTEGER, 
                 type TEXT, 
                 category TEXT, 
                 amount REAL,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')
    
    conn.commit()
    conn.close()
    print("Database setup complete. Tables created successfully.")

if __name__ == "__main__":
    setup_db()