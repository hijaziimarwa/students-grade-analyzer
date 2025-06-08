nb_of_students = int(input("Please enter the number of the students: "))
names_list = []
grades_list = []

for i in range(nb_of_students):
    name = input("Enter the student's name: ")
    grade = int(input("Enter the student's grade: "))
    
    if grade <= 100:
        grades_list.append(grade)
        names_list.append(name)
    else:
        print('Please input a grade below 100')

def get_avg_grade(grades):
    total = 0
    for grade in grades:
        total += grade
    avg = total / len(grades)
    return avg

def get_highest_grade(grades):
    max_index = 0
    for i in range(1, len(grades)):
        if grades[i] > grades[max_index]:
            max_index = i
    return max_index