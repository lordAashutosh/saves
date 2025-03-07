import sqlite3

# Step 1: Connect to SQLite (creates a file-based database if not exists)
conn = sqlite3.connect("example.db") #connection
cursor = conn.cursor()

# # Step 2: Create a Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    likes INTEGER NOT NULL
)
""")
conn.commit()

# Step 3: CRUD Operations
# 3.1. CREATE: Add new records
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"User '{name}' added!")

create_user('Abhishek',20)
create_user('Sam',90)
create_user('Manoj',50)
create_user('Ramesh',40)
name = input("User input your name\n")
age = int(input("User input your age\n"))  

# create_user(name, age)

# # 3.2. READ: Fetch records
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

read_users()

# # 3.3. UPDATE: Modify a record
def update_user(user_id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    print(f"User ID '{user_id}' updated!")


# update_user(2, "Sulav",15)
# # 3.4. DELETE: Remove a record
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"User ID '{user_id}' deleted!")

# delete_user(5)

cursor.execute("DELETE FROM users WHERE name = ?", ('Abhishek',))
conn.commit()



# # Close the connection
conn.close()



# DELETE FROM <TABLE_NAME> WHERE <CONDITION>
# SELECT name,id,age FROM users WHERE name=Abhishek