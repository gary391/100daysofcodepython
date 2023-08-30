dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# print(dict[1])
dict[1] = 4

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])