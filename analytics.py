import sqlite3

def show_dashboard(user_id):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    
    c.execute("SELECT SUM(amount) FROM transactions WHERE user_id=? AND type='Income'", (user_id,))
    total_income = c.fetchone()[0] or 0.0
    
    c.execute("SELECT SUM(amount) FROM transactions WHERE user_id=? AND type='Expense'", (user_id,))
    total_expense = c.fetchone()[0] or 0.0
    
    conn.close()
    
    balance = total_income - total_expense
    
    print("\n=== FINANCIAL DASHBOARD ===")
    print(f"Total Income:  Rs. {total_income}")
    print(f"Total Expense: Rs. {total_expense}")
    print(f"Net Balance:   Rs. {balance}")
    print("===========================")