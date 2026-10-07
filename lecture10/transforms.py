from functools import reduce
from dataclasses import dataclass


# ==========================================
# DATA CLASSES - DO NOT MODIFY
# ==========================================

@dataclass
class Order:
    order_id: int
    total: float


@dataclass
class Item:
    name: str
    price: float
    quantity: int


@dataclass
class Account:
    account_id: str
    balance: float


# ==========================================
# EXERCISES
# ==========================================

def convert_celsius_to_fahrenheit(celsius_temps: list[float]) -> list[float]:
    """
    Takes a list of float Celsius temperatures.
    Uses `map()` and a lambda to convert each temperature to Fahrenheit
    using the formula (C * 9/5) + 32, rounded to 2 decimal places.
    Returns the results as a list of floats.
    """
    return list(
        map(lambda c:
            round((c * 9/5) + 32, 2), 
            celsius_temps    
        )
    )


def filter_valid_orders(orders: list[Order], min_amount: float) -> list[Order]:
    """
    Takes a list of Order dataclass objects and a minimum threshold.
    Uses `filter()` and a lambda to keep ONLY orders where `total` is greater than or
    equal to `min_amount`.
    Returns the filtered list of Order objects.
    """
    return list(
        filter(lambda order:
               order.total >= min_amount, 
               orders
        )
    )


def calculate_total_revenue(items: list[Item]) -> float:
    """
    Takes a list of Item dataclass objects.
    Uses `functools.reduce()` and a lambda to compute aggregate revenue
    (price * quantity) across all items, starting with an initial accumulator of 0.0.
    Returns total revenue rounded to 2 decimal places.
    """
    return round(
        reduce(lambda acc, item:
            acc + (item.price * item.quantity),
            items,
            0.0  # initial acc.
        ), 2
    )


def has_overdue_account(accounts: list[Account]) -> bool:
    """
    Takes a list of Account dataclass objects.
    Uses `any()` to determine if AT LEAST ONE account has a negative balance (< 0.0).
    Returns True if an overdue account exists, otherwise False.
    """
    return any(account.balance < 0.0 for account in accounts)


def verify_all_scores_valid(scores: list[int], max_possible: int) -> bool:
    """
    Takes a list of integer test scores and the maximum possible score.
    Uses `all()` to verify whether EVERY score falls strictly within
    the valid range [0, max_possible].
    Returns True if all scores are valid, otherwise False.
    """
    # return all(0 <= score <= max_possible for score in scores)
    return all(score in range(0, max_possible + 1) for score in scores)


def compute_filtered_average(scores: list[int], threshold: int) -> float:
    """
    Takes a list of integer scores and a threshold.
    First, uses `filter()` with a lambda to keep scores strictly greater than `threshold`.
    Then, uses `reduce()` with a lambda to sum the filtered scores.
    Returns the average of the filtered scores rounded to 2 decimal places.
    If no scores meet the threshold, returns 0.0.
    """
    filtered = list(filter(lambda s: s > threshold, scores))
    if not filtered:
        return 0.0
    # total = reduce(lambda acc, val: acc + val, filtered, 0)  # or use sum()
    # return round(total / len(filtered), 2)

    from statistics import mean
    return round(mean(filtered), 2)  # Does not require list() on filter


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

    # 01. Convert Celsius to Fahrenheit (map)
    run_test("test_01_celsius_to_fahrenheit", convert_celsius_to_fahrenheit([0.0, 20.0, 37.0, 100.0]), [32.0, 68.0, 98.6, 212.0])

    # 02. Filter Valid Orders (filter with Order dataclass)
    orders = [Order(1, 150.0), Order(2, 45.5), Order(3, 200.0), Order(4, 99.99)]
    run_test("test_02_filter_valid_orders", filter_valid_orders(orders, 100.0), [Order(1, 150.0), Order(3, 200.0)])

    # 03. Calculate Total Revenue (reduce with Item dataclass)
    cart = [Item("Widget A", 10.0, 2), Item("Widget B", 15.5, 4), Item("Widget C", 5.0, 1)]
    run_test("test_03_calculate_total_revenue", calculate_total_revenue(cart), 87.0)

    # 04. Has Overdue Account (any with Account dataclass)
    run_test("test_04_has_overdue_account_true", has_overdue_account([Account("A1", 120.50), Account("A2", -15.00)]), True)
    run_test("test_04_has_overdue_account_false", has_overdue_account([Account("A1", 0.00), Account("A2", 45.20)]), False)

    # 05. Verify All Scores Valid (all)
    run_test("test_05_verify_all_scores_valid_true", verify_all_scores_valid([85, 92, 100, 0], 100), True)

    # 06. Compute Filtered Average (filter + reduce)
    run_test("test_06_compute_filtered_average", compute_filtered_average([40, 75, 80, 90, 50], 60), 81.67)


if __name__ == '__main__':
    execute_all()