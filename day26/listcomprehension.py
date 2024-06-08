'''
Note that in the first list comprehension for X_non_str, the order is:

expression for item in iterable if condition

and in the last list comprehension for X_str_changed, the order is:

expression1 if condition else expression2 for item in iterable

I always find it hard to remember that expression1 has to be before if and expression2 has to be after else. My head wants both to be either before or after.

I guess it is designed like that because it resembles normal language, e.g. "I want to stay inside if it rains, else I want to go outside"

In plain English the two types of list comprehensions mentioned above could be stated as:

With only if:

    extract_apple for apple in apple_box if apple_is_ripe

and with if/else

    mark_apple if apple_is_ripe else leave_it_unmarked for apple in apple_box
'''

# List Comprehension
# name of the new_list = [new_item for item in list]
numbers = [1,2,3]
# new_list is number + 1
new_list = [n+1
            for n in numbers]

# Conditional list comphrehension
# new_list = [new_item for item in list if test]
# only add to the list if the condition is true
names = ['Sonu', 'Renu', 'Minku', 'Veer', 'Deepa']
