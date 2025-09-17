import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    for i in range(5):  # Retry up to 5 times
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="admin",
                password="pass",
                host="db",  # service name in docker-compose
                cursor_factory=RealDictCursor
            )
            return conn
        except psycopg2.OperationalError:
            import time
            time.sleep(2)  # Wait before retrying
    raise Exception("Could not connect to the database after several attempts.")

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
