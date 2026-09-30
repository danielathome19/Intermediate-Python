"""
Description: 
Read the farm data from the provided data file.

The file begins with the number of hay bales currently available, 
followed by the cost per hay bale. 
Next are the number of corncobs available and the cost per corncob.

The file then gives the number of rows of cow pens and 
the number of cow pens in each row. For each cow, the file provides:
- name
- weight
- pounds of milk produced per day
- hay bales eaten per day
- corncobs eaten per day

Next, the file gives the number of rows of horse pens and 
the number of horse pens in each row. For each horse, the file provides:
- name
- weight
- hay bales eaten per day
- corncobs eaten per day
- number of rides given
- cost per ride

Complete the super class, Animal and then the sub classes, Horse and Cow.
The program should report:
 * the income of the day
 * the cumulative weight of all animals
 * if there is enough food to feed all the animals
 * the cow that makes the most money
 * the horse that makes the least money

The amount of money a cow makes is the money made for milk 
minus the cost of the feed for that animal for that day.
The amount of money a horse makes is the money generated from giving 
rides minus the cost of the feed for that animal for that day.

When a horse gives it name, it always reports it twice.
A pound of milk sells for $0.20.
"""

from animals import Animal, Cow, Horse


def main():
    animals: list[Animal] = []

    with open("lecture8/farm.txt") as f:
        hay, hay_cost = f.readline().split()
        corn, corn_cost = f.readline().split()

        hay, hay_cost, corn, corn_cost = \
            int(hay), float(hay_cost), int(corn), float(corn_cost)

        cow_rows, cow_pens = f.readline().split()
        for _ in range(int(cow_rows) * int(cow_pens)):
            name, weight, milk, hay_eaten, corn_eaten = f.readline().split()
            wow = Cow(name, int(weight), int(milk), int(corn_eaten), int(hay_eaten))
            animals.append(wow)
        f.readline()  # skip blank line

        horse_rows, horse_pens = f.readline().split()
        for _ in range(int(horse_rows) * int(horse_pens)):
            name, weight, hay_eaten, corn_eaten, rides, ride_cost = f.readline().split()
            horse = Horse(name, int(weight), int(corn_eaten), int(hay_eaten), int(rides), float(ride_cost))
            animals.append(horse)
        pass

    income_today = 0.0
    total_weight = 0
    all_corn_eaten = 0
    all_hay_eaten = 0
    min_horse_index = 0
    min_horse_value = float("inf")
    max_cow_index = 0
    max_cow_value = float("-inf")

    for i, animal in enumerate(animals):  # index i, Animal object animal (for + foreach)
        value = animal.get_value(corn_cost, hay_cost)
        income_today += value
        total_weight += animal.weight
        all_corn_eaten += animal.num_corn
        all_hay_eaten += animal.num_haybales
        if isinstance(animal, Cow):
            if value > max_cow_value:
                max_cow_value = value
                max_cow_index = i
        elif isinstance(animal, Horse):
            if value < min_horse_value:
                min_horse_value = value
                min_horse_index = i

    print(f"Income today: ${income_today:.2f}")
    print(f"Cumulative weight of all animals: {total_weight} lbs")
    print(f"Enough food to feed all animals: {all_corn_eaten <= corn and all_hay_eaten <= hay}")
    print(f"Cow {animals[max_cow_index].get_name()} makes the most money")
    print(f"Horse {animals[min_horse_index].get_name()} makes the least money")

    pass


if __name__ == "__main__":
    main()
