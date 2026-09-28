""" Description:
Keeps track of all of the people in an organization. Within the 
organization are a bunch of people who all have first and last names.
These people are either:
 * students, who have a GPA (double), 
 * teachers, who have a number of students that they teach (int), or 
 * administrators, who have a favorite word (string).

Calculates and displays the following:
* the average GPA, 
* the total number of students taught by the teachers, and 
* the biggest and smallest favorite word among the administrative staff.

The data file will be denoted by a 1 for student, 2 for teacher, and 3 for admin.
There will be a 99 to signify the end of the data file.


Sample output:
Average student GPA: #.##
Total students taught by teachers: ###
Smallest favorite admin word: ...
Largest favorite admin word: ...
"""

from people import *  # import all classes from people.py


def main():
    people: list[Person] = []

    with open("lecture7/school.txt", 'r') as f:
        lines = f.readlines()
        code = int(lines[0])

        idx = 1
        while code != 99:
            fname = lines[idx].strip()
            lname = lines[idx + 1].strip()
            p: Person

            match code:
                case 1:  # Student
                    gpa = float(lines[idx + 2])
                    p = Student(fname, lname, gpa)
                case 2:  # Teacher
                    students = int(lines[idx + 2])
                    p = Teacher(fname, lname, students)
                case 3:  # Admin:
                    fav_word = lines[idx + 2].strip()
                    p = Admin(fname, lname, fav_word)
            people.append(p)
            code = int(lines[idx + 3])
            idx += 4  # skip over 3 lines of info + next person code

    gpa_sum = 0.0
    gpa_cnt = 0
    tot_stu = 0
    large_w = ""
    small_w = "ksjdhgkj;sgh;ksjhns;nk;vin;ovins;ksnbklgjsd;gkjdhg;oiuwbgiowshoishfgoisdhg;ksdg"

    for p in people:
        if isinstance(p, Student):
            gpa_sum += p.gpa
            gpa_cnt += 1
        elif isinstance(p, Teacher):
            tot_stu += p.num_students
        elif isinstance(p, Admin):
            word = p.fav_word
            if len(word) > len(large_w):
                large_w = word
            if len(word) < len(small_w):
                small_w = word

    print(f"Average student GPA: {gpa_sum/gpa_cnt:.2f}")
    print(f"Total students taught by teachers: {tot_stu}")
    print(f"Smallest favorite admin word: {small_w}")
    print(f"Largest favorite admin word: {large_w}")
    pass


if __name__ == "__main__":
    main()
