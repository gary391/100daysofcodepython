# Class are named using PascalCase
# Python used snake or Pascal case

class User:
    def __init__(self, user_id, user_name):
        print("new user being created...")
        self.id = user_id
        self.username = user_name
        self.followers = 0  # The default value, using this we don't have to pass the attribute every time create an
        # object if we don't have the value before hand.
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")

print(user_1.id)
print(user_1.username)

user_2 = User("002", "jack")
print(user_2.id)
print(user_2.username)


user_1.follow(user_2)
print(f"user_1 follower:{user_1.followers}")
print(f"user_1 following: {user_1.following}")
print(f"user_2 follower:{user_2.followers}")
print(f"user_2 following: {user_2.following}")

