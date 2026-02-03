from db import get_connection

def add_task(title, description):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO tasks (title, description) VALUES (%s, %s)"
    cursor.execute(query, (title, description))
    conn.commit()
    conn.close()

def view_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET status='completed' WHERE id=%s",
        (task_id,)
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()

