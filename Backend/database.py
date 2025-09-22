import sqlite3

DB_NAME = "goals.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_goals():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, goal FROM goals")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "goal": r[1]} for r in rows]

def add_goal(goal_text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO goals (goal) VALUES (?)", (goal_text,))
    conn.commit()
    conn.close()

def delete_goal(goal_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
    conn.commit()
    conn.close()