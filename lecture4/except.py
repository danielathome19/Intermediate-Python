# ==========================================
# EXERCISES
# ==========================================

def safe_parse_int(value_str: str, default: int) -> int:
    """
    1. try/except
    Attempts to convert a string to an integer.
    If a ValueError occurs during conversion, 
        catches the exception and returns `default`.
    """
    try:
        parsed = int(value_str)
        return parsed
    except ValueError:
        return default
    pass


def calculate_reciprocal_ratio(num_str: str, den_str: str) -> str:
    """
    2. try/except/except
    Converts two string inputs to floats and calculates 100.0 / (num - den).
    - Catches ValueError if string-to-float conversion fails and 
        returns "Invalid number format".
    - Catches ZeroDivisionError if num equals den and
        returns "Division by zero".
    """
    try:
        num = float(num_str)
        den = float(den_str)
        result = 100.0 / (num - den)
        return f"Result: {round(result, 2)}"
    except ValueError:
        return "Invalid number format"
    except ZeroDivisionError:
        return "Division by zero"
    pass


def process_bank_withdrawal(balance: float, amount: float, audit_log: list[str]) -> float:
    """
    3. try/except/finally
    Attempts to withdraw an amount from a bank balance.
    
    - try: Checks if amount is negative or exceeds balance. If invalid, raises 
           a ValueError with the message "Invalid withdrawal amount.". 
           Otherwise, subtracts amount from balance.
    - except ValueError: Catches the ValueError and appends "Error: <exception_message>" 
                         to audit_log.
    - finally: Appends "Withdrawal attempt logged." to audit_log regardless of 
               whether an exception occurred.
               
    Returns the updated balance (or original balance if withdrawal failed).
    """
    try:
        if amount < 0 or amount > balance:
            raise ValueError("Invalid withdrawal amount.")
        balance -= amount
    except ValueError as e:
        audit_log.append(f"Error: {e}")
    finally:
        audit_log.append("Withdrawal attempt logged.")
    return balance


def parse_and_apply_bonus(raw_score: str, bonus: float) -> tuple[bool, float]:
    """
    4. try/except/else
    Converts raw_score to a float using try/except/else.
    - try: attempts to parse float.
    - except ValueError: catches parsing error and returns (False, 0.0).
    - else: executes ONLY if try block succeeded without exceptions, 
            applies bonus, and returns (True, total).
    """
    try:
        score = float(raw_score)
    except ValueError:
        return (False, 0.0)
    else:
        total = score + bonus
        return (True, total)
    pass


def safe_batch_transform(items: list[str], status_tracker: list[str]) -> list[int]:
    """
    5. try/except/else/finally
    Converts a list of string elements to integers in batch.
    
    - try: Iterates through items and converts each string to an int, adding to a new list.
    - except ValueError: Catches conversion failure, resets the result list to empty [], 
                        and appends "Failed: Invalid data encountered." to status_tracker.
    - else: Runs ONLY if all items converted successfully. Appends "Success: All items converted." 
            to status_tracker.
    - finally: Appends "Batch processing completed." to status_tracker regardless of outcome.
    
    Returns the transformed list of integers (or empty [] if an error occurred).
    """
    output = []

    try:
        for item in items:
            output.append(int(item))
    except ValueError:
        output = []
        status_tracker.append("Failed: Invalid data encountered.")
    else:
        status_tracker.append("Success: All items converted.")
    finally:
        status_tracker.append("Batch processing completed.")
    
    return output


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
    print("Starting exception handling tests...\n")
    
    # 01. try/except
    run_test("test_01_safe_parse_int('42', 0)", safe_parse_int('42', 0), 42)
    run_test("test_01_safe_parse_int('abc', 0)", safe_parse_int('abc', 0), 0)
    
    # 02. try/except/except
    run_test("test_02_reciprocal_ratio_valid", calculate_reciprocal_ratio("10", "6"), "Result: 25.0")
    run_test("test_02_reciprocal_ratio_value_error", calculate_reciprocal_ratio("ten", "6"), "Invalid number format")
    run_test("test_02_reciprocal_ratio_zero_div", calculate_reciprocal_ratio("5", "5"), "Division by zero")
    
    # 03. try/except/finally
    log1 = []
    bal1 = process_bank_withdrawal(100.0, 30.0, log1)
    run_test("test_03_withdrawal_success_balance", bal1, 70.0)
    run_test("test_03_withdrawal_success_log", log1, ["Withdrawal attempt logged."])
    
    log2 = []
    bal2 = process_bank_withdrawal(100.0, 150.0, log2)
    run_test("test_03_withdrawal_fail_balance", bal2, 100.0)
    run_test("test_03_withdrawal_fail_log", log2, ["Error: Invalid withdrawal amount.", "Withdrawal attempt logged."])

    # 04. try/except/else
    run_test("test_04_parse_bonus_success", parse_and_apply_bonus("85.5", 5.0), (True, 90.5))
    run_test("test_04_parse_bonus_fail", parse_and_apply_bonus("invalid", 5.0), (False, 0.0))

    # 05. try/except/else/finally
    tracker1 = []
    res1 = safe_batch_transform(["10", "20", "30"], tracker1)
    run_test("test_05_batch_success_result", res1, [10, 20, 30])
    run_test("test_05_batch_success_tracker", tracker1, ["Success: All items converted.", "Batch processing completed."])
    
    tracker2 = []
    res2 = safe_batch_transform(["10", "bad", "30"], tracker2)
    run_test("test_05_batch_fail_result", res2, [])
    run_test("test_05_batch_fail_tracker", tracker2, ["Failed: Invalid data encountered.", "Batch processing completed."])


if __name__ == '__main__':
    execute_all()