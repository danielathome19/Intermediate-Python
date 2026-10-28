import time
from enum import Enum, auto
from functools import wraps
from typing import Callable, Any


# ==========================================
# EXERCISES
# ==========================================

def delay(seconds: float) -> Callable:
    """
    Decorator with arguments that delays the execution of the wrapped function 
    by `seconds` using time.sleep() before executing and returning its result.
    Uses @wraps from functools to preserve original function metadata.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry(retries: int=3, delay_sec: float=0.01) -> Callable:
    """
    Decorator with arguments that retries executing the wrapped function up to 
    `retries` times if an Exception is raised during execution.
    Pauses `delay_sec` seconds between retry attempts.
    Re-raises the final exception if all attempts fail.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries-1:
                        time.sleep(delay_sec)
            raise last_exception
        return wrapper
    return decorator


#: Raised when a rate-limited function exceeds its allowed call threshold.
class RateLimitExceeded(Exception): pass


def rate_limit(max_calls: int) -> Callable:
    """
    Decorator that restricts a function to being called at most `max_calls` times.
    Tracks execution count across calls.
    Raises RateLimitExceeded if invoked beyond `max_calls`.
    """
    def decorator(func):
        call_count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count  # 'nonlocal' refers to the variable in the enclosing scope (decorator)
            if call_count >= max_calls:
                raise RateLimitExceeded(f"Function '{func.__name__}' exceeded "
                                        f"execution limit of {max_calls} calls.")
            call_count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


class UserRole(Enum):
    """Enumeration representing user access roles in an application."""
    GUEST = auto()
    MEMBER = auto()
    MODERATOR = auto()
    ADMIN = auto()


def get_role_permissions(role: UserRole) -> list[str]:
    """
    Accepts a UserRole enum member and returns its assigned permissions using match/case.
    Permission mapping rules:
      - GUEST     -> read
      - MEMBER    -> read, write
      - MODERATOR -> read, write, moderate
      - ADMIN     -> read, write, moderate, admin
    """
    match role:
        case UserRole.GUEST:
            return ['read']
        case UserRole.MEMBER:
            return ['read', 'write']
        case UserRole.MODERATOR:
            return ['read', 'write', 'moderate']
        case UserRole.ADMIN:
            return ['read', 'write', 'moderate', 'admin']
    pass


#: Enumeration representing valid states in an e-commerce order workflow.
OrderStatus = Enum('OrderStatus', 
                   ['PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED', 'CANCELLED'], 
                   module=__name__)


def transition_order_status(current: OrderStatus, action: str) -> OrderStatus:
    """
    Processes an order state transition based on current state and requested action.
    Valid actions:
      - 'pay'     : PENDING -> PROCESSING
      - 'ship'    : PROCESSING -> SHIPPED
      - 'deliver' : SHIPPED -> DELIVERED
      - 'cancel'  : PENDING or PROCESSING -> CANCELLED
    Raises ValueError for any invalid state transitions.
    """
    match (current, action.lower()):
        case (OrderStatus.PENDING, 'pay'):
            return OrderStatus.PROCESSING
        case (OrderStatus.PROCESSING, 'ship'):
            return OrderStatus.SHIPPED
        case (OrderStatus.SHIPPED, 'deliver'):
            return OrderStatus.DELIVERED
        case (OrderStatus.PENDING | OrderStatus.PROCESSING, 'cancel'):
            return OrderStatus.CANCELLED
        case _:  # otherwise/default
            raise ValueError(f"Invalid transition: Cannot perform "
                             f"action '{action}' on order in state {current.name}.")
    pass


# ==========================================
# TESTS - DO NOT MODIFY
# ==========================================

# Test Target Decorators
@delay(seconds=0.01)
def fetch_api_data(endpoint: str) -> dict:
    return {"status": 200, "endpoint": endpoint}


attempts_count = 0

@retry(retries=3, delay_sec=0.001)
def flaky_service() -> str:
    global attempts_count
    attempts_count += 1
    if attempts_count < 3:
        raise ConnectionError("Service temporarily unavailable")
    return "SUCCESS"


@rate_limit(max_calls=2)
def perform_action(user_id: int) -> str:
    return f"Action complete for user {user_id}"


def run_test(test_name: str, actual, expected) -> None:
    print(f"--- {test_name} ---")
    print(f"Output: {actual}")
    matches = actual == expected
    GREEN, RED, RESET = '\033[92m', '\033[91m', '\033[0m'
    print(f"Matches expected: {GREEN if matches else RED}{matches}{RESET}" + 
          ("\n" if matches else f"; expected {expected}\n"))


def execute_all():
    print("Starting tests...\n")
    
    # 01. Delay Decorator
    run_test("test_01_delay_decorator", fetch_api_data("/users"), {"status": 200, "endpoint": "/users"})

    # 02. Retry Decorator
    run_test("test_02_retry_decorator", flaky_service(), "SUCCESS")

    # 03. Rate Limiter Decorator & Custom Exception
    run_test("test_03_rate_limit_call1", perform_action(101), "Action complete for user 101")
    run_test("test_03_rate_limit_call2", perform_action(102), "Action complete for user 102")
    try:
        perform_action(103)
        rate_limit_passed = False
    except RateLimitExceeded:
        rate_limit_passed = True
    run_test("test_03_rate_limit_exceeded_exception", rate_limit_passed, True)

    # 04. UserRole Enum & Permission Mapping
    run_test("test_04_user_role_guest", get_role_permissions(UserRole.GUEST), ["read"])
    run_test("test_04_user_role_admin", get_role_permissions(UserRole.ADMIN), ["read", "write", "moderate", "admin"])

    # 05. Enum State Machine
    s1 = transition_order_status(OrderStatus.PENDING, "pay")
    s2 = transition_order_status(s1, "ship")
    run_test("test_05_enum_state_transition", (s1, s2), (OrderStatus.PROCESSING, OrderStatus.SHIPPED))
    try:
        transition_order_status(OrderStatus.SHIPPED, "cancel")
        invalid_trans_passed = False
    except ValueError:
        invalid_trans_passed = True
    run_test("test_05_enum_invalid_transition", invalid_trans_passed, True)


if __name__ == '__main__':
    execute_all()