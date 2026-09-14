"""
Description:
In one business the commission paid to each salesperson is based on the 
product line sold and the total amount of the sales. 
Assume that the product line is indicated by a code that can be 5, 8 or 17.

If the code is 5 or 8, the commission rate is 7 1/2% for the first $5000 of sales 
and 8 1/2% for sales over $5000. However, if the product line code is 17, then the 
commission rate is 9 1/2% for the first $3500 of sales and 12% for sales over $3500.
Invalid codes should be checked.

Write a program to determine the commission for each sales person.
Input is the salesperson's ID number, product line code, and total sales.
Output should be the ID number, total sales, and commission with appropriate headings.
	
Sample output:
Number  Code  Sales  Commission
101	    17    2250   213.75
103  	5  	  4000   300.00
117  	3  	  7350   Bad Code
118  	8  	  7350   574.75
125  	5  	  6500   502.50
138 	17    6375   677.50
192  	8  	  8125   640.625
203  	8  	  3250   243.75
218  	5  	  5000   375.00
235  	5  	  5250   396.25
264 	17    4150   410.50
291 	17    750  	 71.25
"""
import csv
from dataclasses import dataclass

@dataclass
class Salesperson:
    id_number: int
    product_code: int
    total_sales: float


def calc_commission(p: Salesperson) -> float | None:
    if p.product_code in (5, 8):
        if p.total_sales <= 5000:
            return p.total_sales * 0.075
        else:
            return (5000 * 0.075) + ((p.total_sales - 5000) * 0.085)
    elif p.product_code == 17:
        if p.total_sales <= 3500:
            return p.total_sales * 0.095
        else:
            return (3500 * 0.095) + ((p.total_sales - 3500) * 0.12)
    else:
        return None  # Bad code


def main():
    with open('lecture3/sales.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        print("Number\tCode\tSales\tCommission")
        for row in reader:
            id, code, sales = int(row[0]), int(row[1]), float(row[2])
            person = Salesperson(id, code, sales)
            commission = calc_commission(person) or "Bad Code"
            # 'or' lets us coalesce a "None" return into a different value
            print(f"{person.id_number}\t" +
                  f"{person.product_code}\t" +
                  f"{person.total_sales}\t" +
                  f"{commission}")
    pass


if __name__ == "__main__":
    main()
