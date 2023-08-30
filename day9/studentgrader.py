"""
This is the scoring criteria:
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
"""
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
# for k,v in student_scores.items():
#     if (v >=91 and v <= 100):
#         v = "Outstanding"
#     elif (v >= 81 and v <= 90):
#         v = "Exceeds Expectations"
#     elif (v >= 71 and v <= 80):
#         v = "Acceptable"
#     elif(v <= 70):
#         v = "Fail"
#     student_grades[k] = v

for student in student_scores:
    score = student_scores[student]
    if(score > 90): # Here we are identifying the value and then adding the value
        student_grades[student] = "Outstanding"
    elif(score > 80):
        student_grades[student] = "Exceeds Expectations"
    elif(score > 70):
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)