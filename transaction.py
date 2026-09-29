import sqlite3

def add_transaction(user_id):
    t_type = input("Is this 'Income' or 'Expense'? ").capitalize()
    if t_type not in ['Income', 'Expense']:
        print("Invalid type. Please enter 'Income' or 'Expense'.")
        return

    category = input("Enter Category (e.g., Salary, Food, Rent): ")
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
        
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (user_id, type, category, amount) VALUES (?, ?, ?, ?)", 
              (user_id, t_type, category, amount))
    conn.commit()
    conn.close()
    print(f"\nSuccess: {t_type} of Rs.{amount} added under '{category}'.")

def view_history(user_id):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("SELECT type, category, amount FROM transactions WHERE user_id=?", (user_id,))
    records = c.fetchall()
    conn.close()
    
    print("\n--- Your Transaction History ---")
    if not records:
        print("No transactions found.")
    else:
        for r in records:
            print(f"Type: {r[0]} | Category: {r[1]} | Amount: Rs.{r[2]}")
    print("--------------------------------")