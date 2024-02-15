# pro to enter the name and percentage of marks in a dictionary and display info on the screen
students_name = int(input("Enter number of students in class"))
marks = {}

for i in range(students_name):
    name = input("Enter the students name :")
    percentage = int(input("Enter the percentage :"))
    marks[name] = percentage

for student in marks:
    print(student, str(marks_list[student])+"%")