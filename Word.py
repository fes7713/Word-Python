from datetime import date, timedelta
from docx import Document
import os

DAYS = d = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

days = 0
course_day = []
course_title = []
d1 = date.today()
print(d1)
starting_day = 0


def input_system():
    global d1, course_day, course_title, days, starting_day  # can we do like this??

    d1_temp = input("Starting date (year month day) : ").split()
    d1 = date(int(d1_temp[0]), int(d1_temp[1]), int(d1_temp[2]))

    d2_temp = input("Ending date   (year month day) : ").split()
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


def date_valid(course_day, day):  # Keita
    for i in range(len(course_day)):
        if course_day[i] == day:
            return True
    return False


def create_folder(course_title):
    if not os.path.exists(course_title):
        os.mkdir(course_title)


def create_file(date, course_title):
    month_arr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    suffix_date_dict = {0: "th", 1: "st", 2: "nd", 3: "rd", 4: "th"}

    suffix_date = suffix_date_dict[date.day % 10 if date.day % 10 < 4 else 4]

    document = Document()
    heading = str(month_arr[date.month - 1]) + " " + str(date.day) + suffix_date + " " + course_title
    document.add_paragraph(heading)
    document.save(course_title + "/" + heading + ".docx")


WEEK = 7

input_system()

for i in range(len(course_title)):
    create_folder(course_title[i])

for n in range(days):
    day = (starting_day + n) % WEEK

    for i in range(len(course_day)):
        if (date_valid(course_day[i], day)):
            print(course_title[i], end=" ")
            print(d1 + timedelta(n))
            create_file(d1 + timedelta(n), course_title[i])

