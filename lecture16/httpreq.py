import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


# ==========================================
# EXERCISES
# ==========================================

def fetch_user_todos(user_id: int) -> list[dict]:
    """
    Retrieves all to-do items assigned to a specific user.
    Appends query parameters (`params=`) and custom request headers (`headers=`).
    Calls `response.raise_for_status()` to handle any HTTP errors (4xx/5xx).
    Returns the parsed JSON response body as a list of dictionaries.
    """
    endpoint = f"{BASE_URL}/todos"
    query_params = {'userId': user_id}
    custom_headers = {'User-Agent': 'CS218-Lecture/1.0'}

    try:
        response = requests.get(
            endpoint, params=query_params, headers=custom_headers, timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"GET request failed: {e}")
        return []


def create_new_album(title: str, user_id: int) -> dict:
    """
    Submits a JSON payload to create a new album resource on the server.
    Uses the `json=` parameter to serialize the payload and set Content-Type header.
    Returns the created resource dictionary returned by the server.
    """
    endpoint = f"{BASE_URL}/albums"
    payload = {
        "title": title,
        "userId": user_id
    }

    try:
        response = requests.post(endpoint, json=payload, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"POST request failed: {e}")
        return {}


def update_todo_completion(todo_id: int, completed: bool) -> dict:
    """
    Partially modifies an existing to-do item by updating only its completion status.
    Differs from PUT, which requires replacing the entire resource payload.
    Returns the updated resource dictionary.
    """
    endpoint = f"{BASE_URL}/todos/{todo_id}"
    patch_data = {'completed': completed}

    try:
        response = requests.patch(endpoint, json=patch_data, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"PATCH request failed: {e}")
        return {}


def remove_album(album_id: int) -> bool:
    """
    Sends an HTTP DELETE request to remove an album at the specified endpoint.
    Returns True if the response status indicates success (200 OK or 204 No Content).
    """
    endpoint = f"{BASE_URL}/albums/{album_id}"

    try:
        response = requests.delete(endpoint, timeout=5)
        response.raise_for_status()
        return response.status_code in (200, 204)
    except requests.RequestException as e:
        print(f"DELETE request failed: {e}")
        return False


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
    
    # 01. GET Request with Query Parameters
    todos = fetch_user_todos(user_id=1)
    run_test("test_01_fetch_user_todos_count", len(todos), 20)
    run_test("test_01_fetch_user_todos_first_id", todos[0].get("id") if todos else None, 1)

    # 02. POST Request (Create)
    created_album = create_new_album(title="CS218 Network Fundamentals", user_id=1)
    run_test("test_02_create_album_id", created_album.get("id"), 101)
    run_test("test_02_create_album_title", created_album.get("title"), "CS218 Network Fundamentals")

    # 03. PATCH Request (Partial Update)
    patched_todo = update_todo_completion(todo_id=1, completed=True)
    run_test("test_03_update_todo_completion", patched_todo.get("completed"), True)

    # 04. DELETE Request
    deleted = remove_album(album_id=1)
    run_test("test_04_remove_album_success", deleted, True)


if __name__ == '__main__':
    execute_all()
