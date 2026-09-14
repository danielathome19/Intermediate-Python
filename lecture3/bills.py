"""
Description:
Utility rates vary with the amount of energy used per month.
One utility company sells electricity at a rate of 7 cents per 
kilowatt hour for the first 2000 hours, 5 cents/kwh for the next 8000 hours, 
and 4 cents for all kwh over 10000 hours.

Write a program that will compute electric bills for any amount of electricity used in a month.
The last value in your file will be the terminal value -999 and should not be processed.

Sample output:
 The cost of 1338 hours is $93.66
 The cost of 9631 hours is $521.55
 The cost of 13561 hours is $682.44
"""


def main():
    kwh = []

    with open('lecture3/bills.txt') as f:
        for line in f:
            hours = int(line)
            if hours != -999:
                kwh.append(hours)
            else:
                break  # exit loop early
        pass

    bills = []
    for hours in kwh:
        cost: float
        if hours <= 2000:
            cost = 0.07 * hours
        elif hours <= 10_000:
            cost = (0.07 * 2000) + (0.05 * (hours-2000))
        else:
            cost = (0.07 * 2000) + (0.05 * 8000) + (0.04 * (hours-10_000))
        bills.append(cost)

    # for i in range(len(kwh)):
    #     print("kwh: " + kwh[i] + " cost: " + bills[i])

    for hours, cost in zip(kwh, bills):
        # Zip iterates through two lists in parallel as a list of tuples
        print(f"The cost of {hours} is ${cost:.2f}")

    pass


if __name__ == "__main__":
    main()
