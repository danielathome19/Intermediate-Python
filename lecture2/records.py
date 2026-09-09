import math
from collections import namedtuple
from dataclasses import dataclass


# ==========================================
# EXERCISES
# ==========================================

# 1. Define a namedtuple called 'Color' with fields 'r', 'g', and 'b'
Color = namedtuple("Color", ['r', 'g', 'b'])
""" Alternatively:
from typing import NamedTuple
class Color(NamedTuple):
    r: int = 255
    g: int
    b: int
"""

def blend_colors(c1: Color, c2: Color, weight: float) -> Color:
    """
    Takes two Color namedtuples and a float weight (between 0.0 and 1.0).
    Blends the two colors based on the weight using the formula:
    new_value = (color1_value * (1 - weight)) + (color2_value * weight)
    
    Calculates this for r, g, and b. 
    Rounds the results to the nearest integer and returns a **new** Color namedtuple.
    """
    new_r = round((c1.r * (1 - weight)) + (c2.r * weight))
    new_g = round((c1.g * (1 - weight)) + (c2.g * weight))
    new_b = round((c1.b * (1 - weight)) + (c2.b * weight))
    return Color(new_r, new_g, new_b)


# 2. Define a dataclass called 'InventoryItem' with fields
# sku (str), total_stock (int), and reserved_stock (int)
@dataclass
class InventoryItem:
    sku: str
    total_stock: int
    reserved_stock: int


def process_order(item: InventoryItem, request_amount: int) -> bool:
    """
    Takes an InventoryItem dataclass and an integer amount requested by a customer.
    Available stock is calculated as: total_stock - reserved_stock.
    
    Logic:
    - If the request_amount is <= 0, return False (invalid order).
    - If the request_amount is greater than the available stock, return False (cannot fulfill).
    - If the request_amount **can** be fulfilled, add the amount to reserved_stock 
      and return True.
    """
    if request_amount <= 0:
        return False

    avail_stock = item.total_stock - item.reserved_stock
    if request_amount > avail_stock:
        return False

    item.reserved_stock += request_amount
    return True


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
    
    # 01. Blend Colors (namedtuple)
    red = Color(255, 0, 0)
    blue = Color(0, 0, 255)
    
    run_test("test_01_blend_colors(red, blue, 0.5)", blend_colors(red, blue, 0.5), Color(128, 0, 128))
    run_test("test_01_blend_colors(red, blue, 0.1)", blend_colors(red, blue, 0.1), Color(230, 0, 26))
    run_test("test_01_blend_colors(red, blue, 1.0)", blend_colors(red, blue, 1.0), Color(0, 0, 255))

    # 02. Process Order (dataclass)
    item1 = InventoryItem("SKU-123", total_stock=50, reserved_stock=40)
    
    # Try to order 15 (only 10 available) -> should fail and stock remains unchanged
    run_test("test_02_process_order(15) - Fails", process_order(item1, 15), False)
    run_test("test_02_check_stock_unchanged", item1.reserved_stock, 40)
    
    # Try to order negative amount -> should fail
    run_test("test_02_process_order(-5) - Fails", process_order(item1, -5), False)
    
    # Try to order 5 (10 available) -> should succeed and update reserved stock to 45
    run_test("test_02_process_order(5) - Succeeds", process_order(item1, 5), True)
    run_test("test_02_check_stock_updated", item1.reserved_stock, 45)


if __name__ == '__main__':
    execute_all()
