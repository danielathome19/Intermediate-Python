from typing import Generator
from collections.abc import Iterator


# ==========================================
# EXERCISES
# ==========================================

class BatchPaginator(Iterator):
    """
    Custom iterator class that splits a list of item strings into fixed-size batches.
    Implements the Iterator protocol (__iter__ and __next__).
    Raises StopIteration when no more items remain.
    """
    def __init__(self, items: list[str], batch_size: int):
        self.items = items
        self.batch_size = batch_size
        self.index = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        batch = self.items[self.index : self.index + self.batch_size]
        self.index += self.batch_size
        return batch


def filter_severe_logs(logs: list[str], target_level: str) -> Generator[str, None, None]:
    """
    Generator function that parses log lines formatted as "SEVERITY: Message".
    Yields formatted log strings "[SEVERITY] Message" ONLY for logs matching or 
    exceeding the target severity rank.
    Severity ranking: INFO (1) < WARNING (2) < ERROR (3) < CRITICAL (4).
    """
    levels = {'INFO': 1, 'WARNING': 2, 'ERROR': 3, 'CRITICAL': 4}
    target_rank = levels.get(target_level, 1)
    for line in logs:
        if ':' in line:
            level, msg = line.split(':', 1)
            level = level.strip().upper()
            if levels.get(level, 0) >= target_rank:
                yield f"[{level}] {msg.strip()}"
    pass


def cumulative_moving_average(stream: list[float]) -> Generator[float, None, None]:
    """
    Generator function demonstrating lazy evaluation.
    Accepts a list/stream of float numbers and yields the running cumulative average
    after processing each element, rounded to 2 decimal places.
    """
    total = 0.0
    count = 0
    for val in stream:
        total += val
        count += 1
        yield round(total / count, 2)
    pass


def sanitize_email_stream(emails: list[str]) -> Generator[str, None, None]:
    """
    Takes a list of raw email strings.
    Returns a generator expression (using parentheses) that strips whitespace, 
    converts text to lowercase, and retains ONLY email strings containing '@' 
    and ending with '.com' or '.edu'.
    """
    cleaned = (email.strip().lower() for email in emails)
    return (
        email for email in cleaned 
        if '@' in email and (email.endswith('.com') or 
                             email.endswith('.edu'))
    )


def flatten_department_rosters(departments: list[list[str]]) -> Generator[str, None, None]:
    """
    Accepts a nested list of departmental employee rosters (list of list of strings).
    Uses the `yield from` expression to delegate iteration to each sublist, 
    yielding individual employee names sequentially.
    """
    for roster in departments:
        yield from roster


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
    
    # 01. Custom Iterator Class: BatchPaginator
    paginator = BatchPaginator(["TaskA", "TaskB", "TaskC", "TaskD", "TaskE"], 2)
    run_test("test_01_batch_paginator_first_next", next(paginator), ["TaskA", "TaskB"])
    run_test("test_01_batch_paginator_drain", list(paginator), [["TaskC", "TaskD"], ["TaskE"]])

    # 02. Generator Function: filter_severe_logs
    log_input = [
        "INFO: Server started on port 8080",
        "ERROR: Database connection timed out",
        "WARNING: CPU usage above 85%",
        "CRITICAL: Out of memory exception"
    ]
    severe_res = list(filter_severe_logs(log_input, "WARNING"))
    expected_severe = [
        "[ERROR] Database connection timed out",
        "[WARNING] CPU usage above 85%",
        "[CRITICAL] Out of memory exception"
    ]
    run_test("test_02_filter_severe_logs", severe_res, expected_severe)

    # 03. Lazy Accumulating Generator: cumulative_moving_average
    telemetry_data = [10.0, 20.0, 30.0, 40.0, 15.0]
    cma_res = list(cumulative_moving_average(telemetry_data))
    expected_cma = [10.0, 15.0, 20.0, 25.0, 23.0]
    run_test("test_03_cumulative_moving_average", cma_res, expected_cma)

    # 04. Generator Expression: sanitize_email_stream
    email_data = ["  ALICE@uww.edu  ", "bob@gmail.org", "charlie@company.com ", "invalid-email"]
    sanitized_gen = sanitize_email_stream(email_data)
    run_test("test_04_sanitize_email_stream", list(sanitized_gen), ["alice@uww.edu", "charlie@company.com"])

    # 05. Delegating Generator: flatten_department_rosters
    dept_rosters = [["Alice", "Bob"], ["Charlie"], ["Dave", "Eve"]]
    flattened_gen = flatten_department_rosters(dept_rosters)
    run_test("test_05_flatten_department_rosters", list(flattened_gen), ["Alice", "Bob", "Charlie", "Dave", "Eve"])


if __name__ == '__main__':
    execute_all()