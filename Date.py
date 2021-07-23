from datetime import date, timedelta
from enum import Enum

# class Day_String_Con(Enum):
#     Mon = 0
#     Monday = 0
#     Tue = 1
#     Tuesday = 1

DAYS = d = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun' : 6}

d = date(2018, 8, 15)
# d = date("2018", "8", "15")
def test(date):
    print(date.month)
    print(date.year)
    print(date.day)
test(d)

test(d + timedelta(30))

a = []
print(a)
b = [0, 1, 2]
a.append(b)
print(a)
b = [3, 4, 5]
a.append(b)
print(a)


def input_system():
    global d1, course_day, course_title, days, starting_day  # can we do like this??

    d1_temp = input("Starting date (year month day) : ").split()
    d1 = date(int(d1_temp[0]), int(d1_temp[1]), int(d1_temp[2]))

    d2_temp = input("Starting date (year month day) : ").split()
    d2 = date(int(d2_temp[0]), int(d2_temp[1]), int(d2_temp[2]))

    days = (d2 - d1).days
    starting_day = d1.weekday()  # this gives a day of specifc date

    nCourse = int(input("How many courses are you taking now : "))
    course_day_temp = []
    for i in range(nCourse):
        course_title.append(input("Course Name : "))

        course_day_temp.append(input("Enter day of class occurrences \n(Mon Tue Wed Thu Fri Sat Sun)\n").split())
        course_day.append([])
        for j in range(len(course_day_temp[i])):
            course_day[i].append(DAYS[course_day_temp[i][j]])
    print(course_day)


d1 = date.today()
days = 0
course_day = []
course_title = []

input_system()