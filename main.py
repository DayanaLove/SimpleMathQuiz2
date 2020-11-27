from classes import Student

student = Student(input("How many questions?"), input("What difficultly do you want?"))
if "easy" in student.get_level():
    student.easy_test()
elif "medium" in student.get_level():
    student.medium_test()
elif "hard" in student.get_level():
    student.hard_test()