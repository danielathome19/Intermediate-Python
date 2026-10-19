import sqlite3

"""
==========================================
GLOBAL DATABASE CONFIGURATION
==========================================

The database will model the following schema for a task management application:
+-----------------------------------------------------------------------+
| Column   | Type    | Description                                      |
|----------|---------|--------------------------------------------------|
| task_id  | INTEGER | Primary key, auto-incremented                    |
| title    | TEXT    | Task title                                       |
| project  | TEXT    | Project name                                     |
| priority | INTEGER | Task priority (1 = Low, 2 = Medium, 3 = High)    |
| status   | TEXT    | Task status ('Todo', 'In Progress', 'Completed') |
| hours    | REAL    | Logged hours                                     |
+-----------------------------------------------------------------------+
All data types should be not null, and the table should be created if it does not already exist.
"""

# DB_FILE = ":memory:"  # Stores database in RAM for testing purposes; will be lost when program exits
DB_FILE = "lecture13/app_tasks.db"  # NOTE: use "SQLite Viewer" extension to inspect file
conn: sqlite3.Connection = None


def init_global_db() -> None:
    """
    Initializes the global database connection and creates the tasks table schema.
    """
    global conn
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            project TEXT NOT NULL,
            priority INTEGER NOT NULL,
            status TEXT NOT NULL,
            hours REAL NOT NULL
        )
    """)
    conn.commit()
    pass


# ==========================================
# EXERCISES
# ==========================================

def add_task(title: str, project: str, priority: int, status: str, hours: float) -> int:
    """
    Inserts a new task record into the global database using parameterized SQL placeholders (?)
    to prevent SQL injection attacks.
    Commits the transaction and returns the auto-generated primary key (cursor.lastrowid).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO tasks (title, project, priority, status, hours)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, project, priority, status, hours)
    )
    conn.commit()
    return cursor.lastrowid


def get_tasks_by_project(project_name: str, min_priority: int) -> list[tuple[int, str, int, str, float]]:
    """
    Queries the database for tasks where (project = project_name) AND (priority >= min_priority).
    Orders results by priority DESC.
    Returns a list of tuples containing: (task_id, title, priority, status, hours).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT task_id, title, priority, status, hours
        FROM tasks
        WHERE project = ? AND priority >= ?
        ORDER BY priority DESC
        """,
        (project_name, min_priority)
    )
    return cursor.fetchall()


def update_task_status_and_hours(task_id: int, new_status: str, new_hours: float) -> bool:
    """
    Updates the status and hours for a task matching task_id using parameterized SQL.
    Commits the transaction.
    Returns True if a row was updated (cursor.rowcount > 0), otherwise False.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE tasks
        SET status = ?, hours = ?
        WHERE task_id = ?
        """,
        (new_status, new_hours, task_id)
    )
    conn.commit()
    return cursor.rowcount > 0


def get_tasks_by_status_and_priority(target_status: str, min_priority: int) -> list[tuple[int, str, str, float]]:
    """
    Queries the database for tasks where (status = target_status) AND (priority >= min_priority).
    Orders results by hours ASC.
    Returns a list of tuples containing: (task_id, title, project, hours).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT task_id, title, project, hours
        FROM tasks
        WHERE status = ? AND priority >= ?
        ORDER BY hours ASC
        """,
        (target_status, min_priority)
    )
    return cursor.fetchall()


def delete_tasks_by_status(status_to_delete: str) -> int:
    """
    Deletes all tasks matching status_to_delete using parameterized SQL.
    Commits the transaction and returns the total number of deleted rows (cursor.rowcount).
    """
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE status = ?",
        (status_to_delete,)
    )
    conn.commit()
    return cursor.rowcount


# ==========================================
# TESTS - DO NOT MODIFY
# ==========================================

def run_test(test_name: str, actual, expected) -> None:
    print(f"--- {test_name} ---")
    print(f"Output: {actual}")
    matches = actual == expected
    GREEN, RED, RESET = '\033[92m', '\033[91m', '\033[0m'
    print(f"Matches expected: {GREEN if matches else RED}{matches}{RESET}" + 
          ("\n" if matches else f"; expected {expected}\n"))


def execute_all():
    print("Starting tests...\n")
    
    # Initialize global database connection and schema
    init_global_db()
    
    # 01. Insert Tasks
    t1 = add_task("Auth Setup", "Web App", 3, "In Progress", 4.5)
    t2 = add_task("UI Refresh", "Web App", 1, "Completed", 2.0)
    t3 = add_task("DB Schema", "Web App", 3, "In Progress", 1.5)
    t4 = add_task("API Tests", "Mobile API", 2, "In Progress", 6.0)
    t5 = add_task("Bug Fixes", "Mobile API", 1, "Completed", 3.0)
    run_test("test_01_add_task_ids", (t1, t2, t3, t4, t5), (1, 2, 3, 4, 5))

    # 02. Query Tasks by Project & Priority (WHERE AND, ORDER BY DESC)
    web_tasks = get_tasks_by_project("Web App", 2)
    expected_web = [
        (1, "Auth Setup", 3, "In Progress", 4.5),
        (3, "DB Schema", 3, "In Progress", 1.5)
    ]
    run_test("test_02_get_tasks_by_project", web_tasks, expected_web)

    # 03. Update Task Status & Hours (UPDATE SET WHERE)
    updated_valid = update_task_status_and_hours(1, "Completed", 7.0)
    updated_invalid = update_task_status_and_hours(99, "Completed", 1.0)
    run_test("test_03_update_task_valid", updated_valid, True)
    run_test("test_03_update_task_invalid", updated_invalid, False)

    # 04. Query Tasks by Status & Priority (ORDER BY ASC)
    completed_high = get_tasks_by_status_and_priority("Completed", 2)
    expected_completed = [(1, "Auth Setup", "Web App", 7.0)]
    run_test("test_04_get_tasks_by_status_and_priority", completed_high, expected_completed)

    # 05. Delete Tasks by Status (DELETE FROM WHERE)
    deleted_count = delete_tasks_by_status("Completed")  # Removes t1 (updated), t2, and t5
    run_test("test_05_delete_tasks_by_status", deleted_count, 3)

    # Clean up connection
    if conn:
        conn.close()


if __name__ == '__main__':
    execute_all()
