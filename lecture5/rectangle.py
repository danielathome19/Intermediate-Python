class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


def main():
    r_len = int(input("Enter length: "))
    r_wid = int(input("Enter width: "))

    rec = Rectangle(r_len, r_wid)

    r_area = rec.area()
    r_perim = rec.perimeter()

    print("Area:", r_area)
    print("Perimeter:", r_perim)
    
    pass


if __name__ == "__main__":
    main()
