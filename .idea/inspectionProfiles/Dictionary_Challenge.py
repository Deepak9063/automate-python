students = {}

for i in range(3):
    name = input("Please enter the name ")
    roll_no = input("Please enter the Roll_number")
    dept = input("please enter the department")

    students[name] = {'roll':roll_no,'dept':dept,'name':name}

print(students)
