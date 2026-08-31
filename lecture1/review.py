import io
import sys
import math
import random
import builtins


# ==========================================
# EXERCISES
# ==========================================

def hello_user() -> None:
    """
    Prompts the user for their name and prints "Hello {name}".
    """
    ...  # TODO


def calculate_mpg(miles: int, gallons: int) -> float:
    """
    Calculates the MPG (rounded to the nearest 10th gal) of a car given its 
    miles and gallons used.
    """
    ...  # TODO


def random_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle using math.pi, then applies a 
    random multiplier between 1.0 and 2.0 using the random module.
    """
    ...  # TODO


def calculate_egg_price(total_eggs: int) -> float:
    """
    Takes a number of eggs and prices them according to:
    [0, 4)  dozen => $0.50/dozen
    [4, 6)  dozen => $0.45/dozen
    [6, 11) dozen => $0.40/dozen
    11+     dozen => $0.35/dozen
    Extra eggs    => 1/12th the per dozen price
    """
    ...  # TODO


def largest_power_of_two(limit: int) -> int:
    """
    Returns the largest power of 2 that is less than or equal to the limit.
    """
    ...  # TODO


def sum_of_squares(n: int) -> int:
    """
    Calculates the sum of all squared numbers from 1 up to and including n.
    """
    ...  # TODO


def filter_positive(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list containing only the positive ones.
    """
    ...  # TODO


def count_vowels(text: str) -> int:
    """
    Returns the integer count of vowels (a, e, i, o, u) in a string, ignoring case.
    """
    ...  # TODO


def generate_report(name: str, scores: list[float]) -> str:
    """
    Calls a function calculate_average(scores: list[float]) to process the scores list, 
    returning a string formatted exactly as:
    "{name} has an average score of {average}."
    """
    average = calculate_average(scores)
    ...  # TODO


# ==========================================
# TESTS - DO NOT MODIFY
# ==========================================

def run_test(test_name: str, actual, expected) -> None:
    """Helper to format output cleanly and handle float comparisons."""
    print(f"--- {test_name} ---")
    print(f"Output: {actual}")
    matches = math.isclose(actual, expected, rel_tol=1e-4) \
        if isinstance(expected, float) and isinstance(actual, (float, int)) \
        else actual == expected
    GREEN, RED, RESET = '\033[92m', '\033[91m', '\033[0m'  # ANSI color codes
    print(f"Matches expected: {GREEN if matches else RED}{matches}{RESET}" + 
          ("\n" if matches else f"; expected {expected}\n"))
    pass


def execute_all():
    print("Starting tests...\n")
    
    # 01. Hello User
    old_input, old_stdout = builtins.input, sys.stdout
    builtins.input = lambda _: 'Alice'  # Override stdin temporarily
    sys.stdout = io.StringIO()
    
    hello_user()
    
    actual_out = sys.stdout.getvalue().strip()
    builtins.input, sys.stdout = old_input, old_stdout  # Restore standard I/O
    run_test("test_01_hello_user", actual_out, "Hello Alice")
    
    # 02. Calculate MPG
    run_test("test_02_calculate_mpg(300, 11)", calculate_mpg(300, 11), 27.3)
    run_test("test_02_calculate_mpg(150, 8)", calculate_mpg(150, 8), 18.8)
    
    # 03. Random Circle Area
    original_uniform = random.uniform
    random.uniform = lambda a, b: 1.5  # Override random.uniform temporarily
    
    expected_area = math.pi * (10 ** 2) * 1.5
    actual_area = random_circle_area(10)
    random.uniform = original_uniform  # Restore random
    run_test("test_03_random_circle_area(10)", actual_area, expected_area)
    
    # 04. Calculate Egg Price
    run_test("test_04_calculate_egg_price(42)", calculate_egg_price(42), 1.75)
    run_test("test_04_calculate_egg_price(60)", calculate_egg_price(60), 2.25)
    run_test("test_04_calculate_egg_price(121)", calculate_egg_price(121), 4.03) 
    run_test("test_04_calculate_egg_price(144)", calculate_egg_price(144), 4.20)
    
    # 05. Largest Power of Two
    run_test("test_05_largest_power_of_two(100)", largest_power_of_two(100), 64)
    run_test("test_05_largest_power_of_two(10)", largest_power_of_two(10), 8)
    run_test("test_05_largest_power_of_two(1)", largest_power_of_two(1), 1)

    # 06. Sum of Squares
    run_test("test_06_sum_of_squares(4)", sum_of_squares(4), 30)
    run_test("test_06_sum_of_squares(1)", sum_of_squares(1), 1)
    
    # 07. Filter Positive
    run_test("test_07_filter_positive([-2, -1, 0, 1, 2])", filter_positive([-2, -1, 0, 1, 2]), [1, 2])
    run_test("test_07_filter_positive([-5, -10])", filter_positive([-5, -10]), [])
    
    # 08. Count Vowels
    run_test("test_08_count_vowels('Hello World')", count_vowels("Hello World"), 3)
    run_test("test_08_count_vowels('AEIOU aeiou')", count_vowels("AEIOU aeiou"), 10)
    
    # 09. Generate Report
    run_test("test_09_generate_report('Bob', [80, 90, 100])", generate_report("Bob", [80, 90, 100]), "Bob has an average score of 90.0.")
    run_test("test_09_generate_report('Charles', [85.5, 90.5])", generate_report("Charles", [85.5, 90.5]), "Charles has an average score of 88.0.")


if __name__ == '__main__':
    execute_all()
