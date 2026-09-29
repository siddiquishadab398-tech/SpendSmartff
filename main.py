import auth, transaction, analytics

def main():
    current_user = None
    
    while True:
        if not current_user:
            print("\n=== SpendSmart Tracker ===")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Select an option: ")
            
            if choice == '1':
                current_user = auth.login()
            elif choice == '2':
                auth.register()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        
        else:
            print("\n=== Main Menu ===")
            print("1. Add Transaction")
            print("2. View History")
            print("3. View Dashboard")
            print("4. Logout")
            choice = input("Select an option: ")
            
            if choice == '1':
                transaction.add_transaction(current_user['id'])
            elif choice == '2':
                transaction.view_history(current_user['id'])
            elif choice == '3':
                analytics.show_dashboard(current_user['id'])
            elif choice == '4':
                current_user = None
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()