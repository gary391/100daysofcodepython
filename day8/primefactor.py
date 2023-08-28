
def prime_checker(number):
    # For a number to be prime, it should be divisible by only two elements
    # factor_count = 0
    # for num in range(1, number + 1):
    #     if (number % num == 0):
    #         factor_count = factor_count + 1
    # if (factor_count == 2):
    #     print("It's a prime number.")
    # else:
    #     print("It's not a prime number.")
    #
    # # Write your code above this line 👆

    is_prime = True
    for num in range(2, number):
        if(number % num == 0):
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
