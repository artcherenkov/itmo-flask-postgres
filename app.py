from flask import Flask, request
from datetime import datetime
import psycopg2
import time

app = Flask(__name__)

# Функция подключения к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database='counter_db',
        user='user',
        password='password'
    )
    return conn

# Функция инициализации базы данных
def init_db():
    retries = 5
    while retries:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS table_counter (
                    id SERIAL PRIMARY KEY,
                    datetime TIMESTAMP NOT NULL,
                    client_info TEXT NOT NULL
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully.")
            break
        except Exception as e:
            print(f"Database connection failed: {e}. Retrying in 3 seconds...")
            time.sleep(3)
            retries -= 1

# Основная функция для обработки запроса
@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        current_time = datetime.now()
        client_info = request.headers.get('User-Agent')

        cursor.execute(
            "INSERT INTO table_counter (datetime, client_info) VALUES (%s, %s)",
            (current_time, client_info)
        )
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM table_counter")
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return f'Hello World! I have been seen {count} times.\n'
    except Exception as e:
        return f"Error: {e}\n"

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)
