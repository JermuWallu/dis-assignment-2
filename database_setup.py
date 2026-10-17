import sqlite3
import random
import os

def create_random_user():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia", "Kevin", "Laura", "Michael", "Nora", "Oliver"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris"]
    age = random.randint(18, 80)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return (first_name, last_name, age)

def create_n_fill_database(db_name):
    # Create/Connect to the database
    print("Creating database: {}".format(db_name))
    conn = sqlite3.connect("databases/{}".format(db_name))
    cursor = conn.cursor()

    # Drop the table if it already exists
    cursor.execute('''DROP TABLE IF EXISTS users''')
    
    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)''')

    # Insert some initial data
    for i in range(5):
        user = create_random_user()
        cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)", user)
        print("Filling {}: added user {}/5".format(db_name, i + 1))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Finished database: {}".format(db_name))

def delete_old_databases():
    # Delete all .db files in the databases directory
    if os.path.exists("databases"):
        for filename in os.listdir("databases"):
            if filename.endswith(".db"):
                os.remove(os.path.join("databases", filename))
                print("Deleted old database: {}".format(filename))
    else:
        print("No 'databases' directory found. No old databases to delete.")

def main():
    print("How many databases you want to create?")
    num_databases = int(input())
    delete_old_databases()
    for i in range(num_databases):
        print("Creating database {}/{}".format(i + 1, num_databases))
        create_n_fill_database("db-{}.db".format(i+1))
        
if __name__ == "__main__":
    main()