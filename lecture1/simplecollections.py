import math


# ==========================================
# EXERCISES
# ==========================================

def multiply_by_index(numbers: list[int]) -> list[int]:
    """
    Takes a list of integers. Returns a new list where each element 
    is multiplied by its original index.
    Example: [5, 10, 15] -> [0, 10, 30]
    """
    result = []  # list()
    for i in range(len(numbers)):
        result.append(numbers[i] * i)
    return result


def split_evens_odds(numbers: list[int]) -> list[list[int]]:
    """
    Takes a list of integers. Returns a list containing exactly two nested lists: 
    the first containing all even numbers, and the second containing all odd numbers.
    Example: [1, 2, 3, 4] -> [[2, 4], [1, 3]]
    """
    evens = []
    odds = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    return [evens, odds]


def get_stats(numbers: list[int]) -> tuple[int, int, int] | None:
    """
    Takes a list of numbers. Calculates the minimum, maximum, and sum.
    Packs and returns these three values in a single immutable tuple in that order.
    Returns None if the list is empty.
    """
    if not numbers:
        return None
    return (min(numbers), max(numbers), sum(numbers))


def swap_coordinates(coords: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Takes a list of (x, y) tuples. Iterates through the list, unpacking 
    each tuple and swapping the values to (y, x). 
    Returns a new list of the swapped tuples.
    """
    swapped = []
    for x, y in coords:
        swapped.append((y, x))
    return swapped


def find_common_elements(list1: list[int], list2: list[int]) -> set[int]:
    """
    Takes two lists. Converts them to sets to find the mathematical intersection 
    (elements present in both). Returns the result as a new Set.
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)  # set1 & set2


def unique_vowels_present(text: str) -> set[str]:
    """
    Takes a string. Finds all unique vowels (a, e, i, o, u) present in the text, 
    ignoring case. Returns them as a Set of lowercase characters.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    text_set = set(text.lower())
    return text_set & vowels



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
    GREEN, RED, RESET = '\033[92m', '\033[91m', '\033[0m'
    print(f"Matches expected: {GREEN if matches else RED}{matches}{RESET}" + 
          ("\n" if matches else f"; expected {expected}\n"))
    pass


def execute_all():
    print("Starting tests...\n")
    
    # 01. Multiply by Index
    run_test("test_01_multiply_by_index([5, 10, 15])", multiply_by_index([5, 10, 15]), [0, 10, 30])
    run_test("test_01_multiply_by_index([1, 1, 1, 1])", multiply_by_index([1, 1, 1, 1]), [0, 1, 2, 3])
    run_test("test_01_multiply_by_index([])", multiply_by_index([]), [])

    # 02. Split Evens and Odds
    run_test("test_02_split_evens_odds([1, 2, 3, 4, 5, 6])", split_evens_odds([1, 2, 3, 4, 5, 6]), [[2, 4, 6], [1, 3, 5]])
    run_test("test_02_split_evens_odds([2, 4, 6])", split_evens_odds([2, 4, 6]), [[2, 4, 6], []])
    run_test("test_02_split_evens_odds([1, 3, 5])", split_evens_odds([1, 3, 5]), [[], [1, 3, 5]])
    run_test("test_02_split_evens_odds([])", split_evens_odds([]), [[], []])

    # 03. Get Stats
    run_test("test_03_get_stats([1, 2, 3, 4, 5])", get_stats([1, 2, 3, 4, 5]), (1, 5, 15))
    run_test("test_03_get_stats([-10, 0, 10])", get_stats([-10, 0, 10]), (-10, 10, 0))
    run_test("test_03_get_stats([42])", get_stats([42]), (42, 42, 42))
    run_test("test_03_get_stats([])", get_stats([]), None)

    # 04. Swap Coordinates
    run_test("test_04_swap_coordinates([(1, 2), (3, 4)])", swap_coordinates([(1, 2), (3, 4)]), [(2, 1), (4, 3)])
    run_test("test_04_swap_coordinates([(-1, 5), (0, 0)])", swap_coordinates([(-1, 5), (0, 0)]), [(5, -1), (0, 0)])
    run_test("test_04_swap_coordinates([])", swap_coordinates([]), [])

    # 05. Find Common Elements
    run_test("test_05_find_common_elements([1, 2, 3], [3, 4, 5])", find_common_elements([1, 2, 3], [3, 4, 5]), {3})
    run_test("test_05_find_common_elements([1, 1, 2], [2, 2, 1])", find_common_elements([1, 1, 2], [2, 2, 1]), {1, 2})
    run_test("test_05_find_common_elements([1, 2], [3, 4])", find_common_elements([1, 2], [3, 4]), set())
    run_test("test_05_find_common_elements([], [1, 2])", find_common_elements([], [1, 2]), set())

    # 06. Unique Vowels Present
    run_test("test_06_unique_vowels_present('Hello World')", unique_vowels_present("Hello World"), {"e", "o"})
    run_test("test_06_unique_vowels_present('QUEUEING')", unique_vowels_present("QUEUEING"), {"u", "e", "i"})
    run_test("test_06_unique_vowels_present('Rhythm')", unique_vowels_present("Rhythm"), set())
    run_test("test_06_unique_vowels_present('AaEeIiOoUu')", unique_vowels_present("AaEeIiOoUu"), {"a", "e", "i", "o", "u"})


if __name__ == '__main__':
    execute_all()