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
def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count

def display_student_summary(names, grades):
    max_index = get_highest_grade(grades)
    count = count_passed(grades)
    avg = get_avg_grade(grades)
    
    print(f'\n{names[max_index]} has the highest grade: {grades[max_index]}')
    print(f'There {"is" if count == 1 else "are"} {count} student{"s" if count != 1 else ""} passed')
    print(f'The average grade is {avg:.2f}')


display_student_summary(names_list, grades_list)
