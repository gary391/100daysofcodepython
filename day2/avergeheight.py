# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
averge_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  averge_height = averge_height + student_heights[n]

final_value = averge_height/len(student_heights)
print(final_value)


#Write your code below this row 👇
