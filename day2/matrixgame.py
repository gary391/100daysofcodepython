# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Convert the input to a usable format
"""
1 --> 0 
2 --> 1
3 --> 2
"""
row = 0
column = 0
split_list = [char for char in  position]
print(type(split_list[0]))
print("Column: " + (split_list[0]))
print("Row: " + (split_list[1]))

if (int(split_list[0]) ==1):
    # 0 Column
    column = 0
if(int(split_list[0]) == 2):
    # 1 Column 
    column = 1    
if(int(split_list[0]) ==3):
    # 2 Column
    column = 2
if(int(split_list[1]) ==1):
    # 0 Row
    row = 0
if(int(split_list[1]) ==2):
    # 1 Row
    row = 1
if(int(split_list[1]) ==3):
    # 2 Row
    row = 2
print(f"New Column: {column}")
print(f"New Row: {row}")
map[row][column] = 'X'
    #
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

