"""
Description:
A municipal parking garage calculates parking fees based on vehicle type 
and total duration (in hours). Each vehicle type uses a tiered hourly rate: 
a standard rate for initial hours up to a threshold, and an overtime rate 
for any hours beyond that threshold.

Rates:
- Type "COMPACT": $2.00/hr up to 4 hrs, $4.00/hr over 4 hrs.
- Type "SUV":     $3.50/hr up to 4 hrs, $6.00/hr over 4 hrs.
- Type "TRUCK":   $5.00/hr up to 2 hrs, $8.50/hr over 2 hrs.
- Any unlisted vehicle type should output "Invalid Type".

Requirements:
1. Write a factory function returning a closure/lambda to calculate tiered parking fees.
2. Store the rate calculators in a dispatch dictionary mapped by vehicle type.
3. Read records from "parking.csv" into a Ticket dataclass.
4. Display a report sorted by calculated fee in descending order using 
   sorted() and a lambda key function.

Sample Output:
Ticket      Type        Hours     Fee
T-104       TRUCK       6.5       $48.25
T-102       SUV         7.0       $32.00
T-106       COMPACT     8.0       $24.00
T-105       SUV         3.5       $12.25
T-101       COMPACT     3.0       $6.00
T-103       EV          5.0       Invalid Type
"""
import csv
from typing import Callable
from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: str
    vehicle_type: str
    hours: float


def make_parking_calculator(base_rate: float, threshold: float, overtime_rate: float) -> Callable[[float], float]:
    """Returns a closure/lambda calculating parking fees based on duration thresholds."""
    return lambda hours: (
        (hours * base_rate)
        if hours <= threshold
        else (threshold * base_rate) + ((hours - threshold) * overtime_rate)
    )


VEHICLE_CALCS = {
    "COMPACT": make_parking_calculator(2.00, 4, 4.00),
    "SUV": make_parking_calculator(3.50, 4, 6.00),
    "TRUCK": make_parking_calculator(5.00, 2, 8.50)
}

def calculate_fee(ticket: Ticket) -> float | None:
    calc = VEHICLE_CALCS.get(ticket.vehicle_type.upper())
    return calc(ticket.hours) if calc else None


def main():
    tickets: list[Ticket] = []

    with open("lecture9/parking.csv", 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            tickets.append(Ticket(row[0], row[1], float(row[2])))

    sorted_tickets = sorted(
        tickets,
        key=lambda t: calculate_fee(t) or -1.0,
        reverse=True
    )
    print("Ticket\tType\tHours\tFee")
    for t in sorted_tickets:
        fee = calculate_fee(t)
        fee_str = f"${fee:.2f}" if fee is not None else "Invalid type"
        print(f"{t.ticket_id}\t{t.vehicle_type}\t{t.hours:.1f}\t{fee_str}")
    
    pass


if __name__ == "__main__":
    main()
