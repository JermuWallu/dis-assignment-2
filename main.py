import os
import database_manager as db_manager

def menu():
    print("Select an option:")
    print("1. View database")
    print("2. Add user")
    print("3. Delete user")
    print("4. Modify user")
    print("5. Check databases status")
    print("0. Exit")
    return int(input("Enter your choice: "))

def check_databases():
    # check if databases dir exists, if not the alert user
    if not os.path.exists("databases"):
        print("The 'databases' directory does not exist. Please create databases by running the database_setup.py first.")
        return False
        
    # check how many databases are in the databases dir and tell the user
    db_files = [f for f in os.listdir("databases") if f.endswith(".db")]
    db_files.sort(key=lambda x: int(x.split('-')[1].split('.')[0]))  # Sort by the number in the filename
    if not db_files:
        print("No databases found in the 'databases' directory. Please create databases by running the database_setup.py first.")
        return False
    print("Found {} database(s): {}".format(len(db_files), ", ".join(db_files)))
    return True

def main():
    print("Welcome to the my program!")
    check_databases()
    while True:
        choice = menu()
        if choice == 1:
            db_name = input("Enter the database name (e.g., database_1): ")
            print("\nViewing database: {}".format(db_name+".db"))
            db_manager.view_db(db_name+".db")
        elif choice == 2:
            db_name = input("Enter the database name (e.g., database_1): ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            print("\nAdding user to database: {}".format(db_name+".db"))
            db_manager.add_user(db_name+".db", first_name, last_name, age)
        elif choice == 3:
            db_name = input("Enter the database name (e.g., database_1): ")
            user_id = int(input("Enter user ID to delete: "))
            print("\nDeleting user from database: {}".format(db_name+".db"))
            db_manager.delete_user(db_name+".db", user_id)
        elif choice == 4:
            db_name = input("Enter the database name (e.g., database_1): ")
            user_id = int(input("Enter user ID to modify: "))
            first_name = input("Enter new first name (or leave blank to keep current): ")
            last_name = input("Enter new last name (or leave blank to keep current): ")
            age = input("Enter new age (or leave blank to keep current): ")
            print("\nModifying user in database: {}".format(db_name+".db"))
            db_manager.modify_user(db_name+".db", user_id, first_name if first_name else None, last_name if last_name else None, int(age) if age else None)
        elif choice == 5:
            check_databases()
        elif choice == 0:
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice. Please try again.")
        print("")
            
if __name__ == "__main__":
    main()