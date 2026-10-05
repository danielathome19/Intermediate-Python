from typing import Callable, Any


# ==========================================
# EXERCISES
# ==========================================

def apply_custom_filter(numbers: list[int], predicate: Callable[[int], bool]) -> list[int]:
    """
    Takes a list of integers and a predicate function (a function taking an int and returning a bool).
    Returns a new list containing ONLY the integers for which predicate(x) evaluates to True.
    """
    return [x for x in numbers if predicate(x) == True]


def create_threshold_filter(threshold: float, keep_above: bool = True) -> Callable[[float], bool]:
    """
    Takes a float threshold and a boolean flag `keep_above`.
    Returns a new function (closure) that takes a single float value and returns True if:
      - `val > threshold` (when keep_above is True)
      - `val < threshold` (when keep_above is False)
    """
    def filter_func(val: float) -> bool:
        if keep_above:
            return val > threshold
        return val < threshold
    return filter_func


def execute_operation(a: float, b: float, operator: str) -> float:
    """
    Takes two floats and a string operator ('+', '-', '*', '/').
    Uses an internal dictionary dispatch table mapping operators to lambda functions.
    Executes the corresponding operation and returns the result rounded to 2 decimal places.
    """
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    return round(ops[operator](a, b), 2)


def sort_records_by_key(records: list[dict[str, Any]], key_name: str, reverse: bool = False) -> list[dict[str, Any]]:
    """
    Takes a list of dictionary records, a key name, and an optional reverse flag.
    Returns a new list of records sorted by the specified dictionary key 
    using `sorted()` and a `lambda` key extraction function.
    """
    return sorted(records, key=lambda record: record[key_name], reverse=reverse)


def find_extreme_record(records: list[dict[str, Any]], key_name: str, find_highest: bool = True) -> dict[str, Any]:
    """
    Takes a list of dictionary records, a target key name, and a boolean flag `find_highest`.
    Uses `max()` or `min()` combined with a `lambda` key extraction function to return 
    the single dictionary record with the maximum or minimum value for that key.
    """
    if find_highest:
        return max(records, key=lambda record: record[key_name])
    return min(records, key=lambda record: record[key_name])


def categorize_scores(scores: list[int], passing_score: int) -> list[str]:
    """
    Takes a list of integer scores and a passing score threshold.
    Applies a `lambda` function containing an inline ternary conditional expression 
    ('PASS' if score >= passing_score else 'FAIL') across all scores.
    Returns a list of formatted string tags (e.g., ["85: PASS", "45: FAIL"]).
    """
    get_tag = lambda score: f"{score}: PASS" if score >= passing_score else f"{score}: FAIL"
    return [get_tag(score) for score in scores]


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
    
    # 01. Apply Custom Filter (Higher-Order Function)
    run_test("test_01_apply_custom_filter_evens", apply_custom_filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0), [2, 4, 6])
    run_test("test_01_apply_custom_filter_positives", apply_custom_filter([-5, 10, -2, 0, 7], lambda x: x > 0), [10, 7])

    # 02. Create Threshold Filter (Returning Functions / Closures)
    above_50 = create_threshold_filter(50.0, keep_above=True)
    below_30 = create_threshold_filter(30.0, keep_above=False)
    run_test("test_02_create_threshold_filter_above", [above_50(val) for val in [20.0, 50.0, 75.0]], [False, False, True])
    run_test("test_02_create_threshold_filter_below", [below_30(val) for val in [15.0, 30.0, 45.0]], [True, False, False])

    # 03. Execute Operation (Dispatch Table)
    run_test("test_03_execute_operation_add", execute_operation(12.5, 3.5, "+"), 16.0)
    run_test("test_03_execute_operation_mult", execute_operation(10.0, 4.25, "*"), 42.5)

    # 04. Sort Records by Key (Lambdas as Key Functions in sorted)
    students = [
        {"name": "Alice", "gpa": 3.8},
        {"name": "Bob", "gpa": 3.2},
        {"name": "Charlie", "gpa": 3.9}
    ]
    expected_sorted = [
        {"name": "Bob", "gpa": 3.2},
        {"name": "Alice", "gpa": 3.8},
        {"name": "Charlie", "gpa": 3.9}
    ]
    run_test("test_04_sort_records_by_key", sort_records_by_key(students, "gpa"), expected_sorted)

    # 05. Find Extreme Record (Lambdas as Key Functions in min/max)
    run_test("test_05_find_extreme_record_highest", find_extreme_record(students, "gpa", find_highest=True), {"name": "Charlie", "gpa": 3.9})
    run_test("test_05_find_extreme_record_lowest", find_extreme_record(students, "gpa", find_highest=False), {"name": "Bob", "gpa": 3.2})

    # 06. Categorize Scores (Lambda with Ternary Condition)
    scores_in = [92, 58, 70, 45]
    tags_out = ["92: PASS", "58: FAIL", "70: PASS", "45: FAIL"]
    run_test("test_06_categorize_scores", categorize_scores(scores_in, 60), tags_out)


if __name__ == '__main__':
    execute_all()