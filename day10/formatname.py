# Write a function to convert a name into a camel case

# Function with outputs
def format_name(f_name, l_name):
    # return f_name.capitalize(),  l_name.capitalize()
    if( f_name == "" or l_name ==""):
        return "You didn't provide valid inputs."# Terminate the function early
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()

    # print(f'{formated_f_name} {formated_l_name}')
    return (f'{formated_f_name} {formated_l_name}')

print(format_name(input("What is your first name? "), input("What is your last name? ")))