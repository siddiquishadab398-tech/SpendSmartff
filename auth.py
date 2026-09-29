import sqlite3

def register():
    username = input("Choose a Username: ")
    password = input("Choose a Password: ")
    
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("\nRegistration Successful! You can now log in.")
    except sqlite3.IntegrityError:
        print("\nError: Username already exists. Please try another.")
    conn.close()

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("SELECT id, username FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    
    if user:
        print(f"\nWelcome back, {user[1]}!")
        return {"id": user[0], "username": user[1]}
    else:
        print("\nInvalid username or password.")
        return None