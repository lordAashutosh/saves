import sqlite3
def create_database():
    """
    Creates a SQLite database with a table to store job information.
    """
    conn = sqlite3.connect("jobs.db")  # Creates or opens jobs.db
    cursor = conn.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company TEXT NOT NULL,
            direct_apply_url TEXT NOT NULL,
            salary TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

create_database()

def insert_job_data(job_title, company, direct_apply_url, salary):
    """
    Inserts job data into the database.
    """
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM jobs WHERE job_title = ?
    ''', (job_title,))

    result = cursor.fetchone()
    if result[0] >0:
        print('Already Exists')
        return

    
    cursor.execute('''
        INSERT INTO jobs (job_title, company, direct_apply_url, salary)
        VALUES (?, ?, ?, ?)
    ''', (job_title, company, direct_apply_url, salary))
    
    conn.commit()
    conn.close()
    print(f"Data inserted: {job_title} at {company}")

    
