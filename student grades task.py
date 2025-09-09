students = [
    {"name": "mohamed", "grade": [85, 95, 92]},
    {"name": "anas", "grade": [75, 85, 80]},
    {"name": "omar", "grade": [90, 88, 84]},
    {"name": "ali", "grade": [70, 60, 65]}
    ]
print("calculate student average grade")
for student in students:
    average = sum(student["grade"]) / len(student["grade"])
    print(f"{student['name']}'s average grade is: {average}")