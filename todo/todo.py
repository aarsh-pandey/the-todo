
import sqlite3


class Todo:

    def __init__(self, db_path):
        self.sqlite_path = db_path
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            );
        """)
        conn.commit()
        conn.close()

    def add_task(self, task):
        with sqlite3.connect(self.sqlite_path) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            conn.commit()

    def get_tasks(self):
        with sqlite3.connect(self.sqlite_path) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM tasks")
            tasks = c.fetchall()
        return tasks

    def complete_task(self, task_id):
        with sqlite3.connect(self.sqlite_path) as conn:
            c = conn.cursor()
            c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
            conn.commit()

    def remove_task(self, task_id):
        with sqlite3.connect(self.sqlite_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            c.execute("UPDATE tasks SET id = id - 1 WHERE id > ?", (task_id,))
            conn.commit()

    def remove_all(self):
        with sqlite3.connect(self.sqlite_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM tasks")
            conn.commit()
