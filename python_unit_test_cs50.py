'''
https://www.youtube.com/watch?v=tIrcxwLqzjQ&ab_channel=CS50
'''

def main():
    # x = int(input("What's x? "))
    x = input("What's x? ")
    print("x square is", square(x))
    

def square(n):
    return n * n

if __name__ == "__main__":
    main()