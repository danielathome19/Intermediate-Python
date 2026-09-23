# ==========================================
# EXERCISES
# ==========================================

class ShippingPackage:
    """
    1. Instance vs. Class Variables & Class Methods
    (E-commerce Logistics)
    
    Class Attributes:
        base_rate (float): Initialized to 5.0 (shared baseline fee).
        
    Methods:
        - __init__(package_id: str, weight_kg: float):
            Initializes instance variables self.package_id and self.weight_kg.
            
        - calculate_shipping_cost(self) -> float:
            Calculates total cost: ShippingPackage.base_rate + (weight_kg * 2.5).
            Returns total rounded to 2 decimal places.
            
        - @classmethod update_base_rate(cls, new_rate: float) -> None:
            Updates the shared class variable cls.base_rate to new_rate.
    """
    base_rate: float = 5.0

    def __init__(self, package_id: str, weight_kg: float) -> None:
        self.package_id = package_id
        self.weight_kg = float(weight_kg)

    def calculate_shipping_cost(self) -> float:
        total = ShippingPackage.base_rate + (self.weight_kg * 2.5)
        return round(total, 2)

    @classmethod
    def update_base_rate(cls, new_rate: float) -> None:
        cls.base_rate = new_rate


class AccessKey:
    """
    2. Static Methods & Class Method Factory Pattern
    (Software Licensing & Security)
    
    Methods:
        - __init__(key_code: str, tier: str):
            Initializes self.key_code and self.tier.
            
        - @staticmethod is_valid_format(key_code: str) -> bool:
            Utility method. Checks if key_code is formatted as "KEY-XXXX-YYYY"
            where XXXX and YYYY are 4-digit numbers. Returns True if valid, else False.
            
        - @classmethod generate_key(cls, key_code: str, tier: str) -> AccessKey:
            Factory method.
            - Calls AccessKey.is_valid_format(key_code). If False, raises ValueError("Invalid license key format.").
            - Checks if tier is "BASIC", "PRO", or "ENTERPRISE". If not, raises ValueError("Invalid tier.").
            - Instantiates and returns a new AccessKey using cls(key_code, tier.upper()).
    """
    def __init__(self, key_code: str, tier: str) -> None:
        self.key_code = key_code
        self.tier = tier

    @staticmethod
    def is_valid_format(key_code: str) -> bool:
        parts = key_code.split('-')
        if len(parts) != 3:
            return False
        if parts[0] != "KEY":
            return False
        if len(parts[1]) != 4 or not parts[1].isdigit():
            return False
        if len(parts[2]) != 4 or not parts[2].isdigit():
            return False
        return True

    @classmethod
    def generate_key(cls, key_code: str, tier: str) -> "AccessKey":
        if not AccessKey.is_valid_format(key_code):
            raise ValueError("Invalid license key format.")
        norm_tier = tier.upper()
        if norm_tier not in ["BASIC", "PRO", "ENTERPRISE"]:
            raise ValueError("Invalid tier.")
        return cls(key_code, norm_tier)


class MediaFile:
    """
    3. String Representations (__str__ vs __repr__)
    (Digital Asset Management)
    
    Methods:
        - __init__(filename: str, file_format: str, size_mb: float):
            Initializes self.filename, self.file_format (uppercase), and self.size_mb.
            
        - __str__(self) -> str:
            Returns user-facing readable string formatted as:
            "<filename> [<file_format> - <size_mb> MB]"
            Example: "tutorial.mp4 [MP4 - 120.5 MB]"
            
        - __repr__(self) -> str:
            Returns developer debugging representation using !r formatted as:
            "MediaFile(<filename!r>, <file_format!r>, <size_mb!r>)"
            Example: "MediaFile('tutorial.mp4', 'MP4', 120.5)"
    """
    def __init__(self, filename: str, file_format: str, size_mb: float) -> None:
        self.filename = filename
        self.file_format = file_format.upper()
        self.size_mb = float(size_mb)

    def __str__(self) -> str:
        return f"{self.filename} [{self.file_format} - {self.size_mb} MB]"

    def __repr__(self) -> str:
        return f"MediaFile({self.filename!r}, {self.file_format!r}, {self.size_mb!r})"


class TimeDuration:
    """
    4. Operator Overloading (__add__ and __eq__)
    (Time Tracking System)
    
    Methods:
        - __init__(hours: int, minutes: int):
            Normalizes hours and minutes (e.g., 90 minutes becomes 1 hour and 30 minutes).
            
        - total_minutes(self) -> int:
            Helper method returning (self.hours * 60) + self.minutes.
            
        - __eq__(self, other) -> bool:
            - If other is not a TimeDuration, returns NotImplemented.
            - Returns True if self.total_minutes() == other.total_minutes().
            
        - __add__(self, other) -> TimeDuration:
            - If other is not a TimeDuration, returns NotImplemented.
            - Adds total minutes together and returns a new normalized TimeDuration object.
            
        - __repr__(self) -> str:
            Returns "TimeDuration(<hours!r>, <minutes!r>)".
    """
    def __init__(self, hours: int, minutes: int) -> None:
        extra_hours = minutes // 60
        self.minutes = minutes % 60
        self.hours = hours + extra_hours

    def total_minutes(self) -> int:
        return (self.hours * 60) + self.minutes

    def __eq__(self, other) -> bool:
        if not isinstance(other, TimeDuration):
            return NotImplemented
        return self.total_minutes() == other.total_minutes()

    def __add__(self, other) -> "TimeDuration":
        if not isinstance(other, TimeDuration):
            return NotImplemented
        combined = self.total_minutes() + other.total_minutes()
        return TimeDuration(0, combined)

    def __repr__(self) -> str:
        return f"TimeDuration({self.hours!r}, {self.minutes!r})"


class TaskItem:
    """
    5. Comparison Overloading (__lt__ and __eq__)
    (Project Task Management)
    
    Methods:
        - __init__(title: str, priority: int, est_hours: float):
            Initializes self.title, self.priority (higher int = higher priority), 
            and self.est_hours.
            
        - __eq__(self, other) -> bool:
            - If other is not a TaskItem, returns NotImplemented.
            - Returns True if title, priority, and est_hours all match.
            
        - __lt__(self, other) -> bool:
            - If other is not a TaskItem, returns NotImplemented.
            - Sorts higher priority tasks BEFORE lower priority tasks (descending priority).
            - If priorities match, sorts by est_hours ascending (shorter tasks first).
            
        - __repr__(self) -> str:
            Returns "TaskItem(<title!r>, <priority!r>, <est_hours!r>)".
    """
    def __init__(self, title: str, priority: int, est_hours: float) -> None:
        self.title = title
        self.priority = int(priority)
        self.est_hours = float(est_hours)

    def __eq__(self, other) -> bool:
        if not isinstance(other, TaskItem):
            raise NotImplemented
        return (self.title == other.title and
                self.priority == other.priority and
                self.est_hours == other.est_hours)

    def __lt__(self, other) -> bool:
        if not isinstance(other, TaskItem):
            raise NotImplemented
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.est_hours < other.est_hours

    def __repr__(self) -> str:
        return f"TaskItem({self.title!r}, {self.priority!r}, {self.est_hours!r})"


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
    print("Starting OOP II tests...\n")
    
    # 01. ShippingPackage (Class vs Instance Members)
    pkg1 = ShippingPackage("PKG-101", 2.0)
    pkg2 = ShippingPackage("PKG-102", 10.0)
    run_test("test_01_pkg_initial_cost", pkg1.calculate_shipping_cost(), 10.0)
    ShippingPackage.update_base_rate(8.0)
    run_test("test_01_pkg_updated_rate_pkg1", pkg1.calculate_shipping_cost(), 13.0)
    run_test("test_01_pkg_updated_rate_pkg2", pkg2.calculate_shipping_cost(), 33.0)
    
    # 02. AccessKey (Static Methods & Factory Pattern)
    run_test("test_02_key_validation_valid", AccessKey.is_valid_format("KEY-1234-5678"), True)
    run_test("test_02_key_validation_bad_prefix", AccessKey.is_valid_format("BAD-1234-5678"), False)
    run_test("test_02_key_validation_short_digits", AccessKey.is_valid_format("KEY-123-5678"), False)
    
    key_obj = AccessKey.generate_key("KEY-9999-0000", "pro")
    run_test("test_02_factory_tier_normalization", key_obj.tier, "PRO")
    
    invalid_key_raised = False
    try:
        AccessKey.generate_key("INVALID-KEY", "pro")
    except ValueError:
        invalid_key_raised = True
    run_test("test_02_factory_invalid_format_raises", invalid_key_raised, True)

    # 03. MediaFile (__str__ and __repr__)
    media = MediaFile("tutorial.mp4", "mp4", 120.5)
    run_test("test_03_str_representation", str(media), "tutorial.mp4 [MP4 - 120.5 MB]")
    run_test("test_03_repr_representation", repr(media), "MediaFile('tutorial.mp4', 'MP4', 120.5)")

    # 04. TimeDuration Operator Overloading (__add__ and __eq__)
    t1 = TimeDuration(1, 45) # 105 mins
    t2 = TimeDuration(0, 75) # 75 mins -> 1 hr 15 mins
    t3 = TimeDuration(3, 0)  # 180 mins
    
    run_test("test_04_time_equality_check", t2 == TimeDuration(1, 15), True)
    run_test("test_04_time_addition", t1 + t2, t3)
    
    # 05. TaskItem Comparison (__lt__ and sorting)
    task1 = TaskItem("Fix critical bug", priority=5, est_hours=2.0)
    task2 = TaskItem("Update documentation", priority=1, est_hours=1.0)
    task3 = TaskItem("Refactor database", priority=5, est_hours=0.5)
    
    tasks = [task2, task1, task3]
    sorted_tasks = sorted(tasks)
    expected_order = [task3, task1, task2] # Priority 5 first (sorted by duration: 0.5 then 2.0), Priority 1 last
    run_test("test_05_task_sorting_priority_and_duration", sorted_tasks, expected_order)


if __name__ == '__main__':
    execute_all()