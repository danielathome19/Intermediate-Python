class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):  # Student extends Person class
    def __init__(self, first, last, gpa):
        super().__init__(first, last)   # Calls Person.__init__()
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, first, last, students):
        super().__init__(first, last)
        self.num_students = students


class Admin(Person):
    def __init__(self, first, last, fav_word):
        super().__init__(first, last)
        self.fav_word = fav_word
