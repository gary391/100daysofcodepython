alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
text = "hello"
# for index, item in enumerate (choices): where choices is a list
#       print(index, item) # This is from the choice list
# This creates a list of tuples, where each tuple is a combination of index and item
index_list = []
for i in text:
    for index, item in enumerate(alphabet):
        if (item == i):
            index_list.append(index)
print(index_list)

shift = 5
shifted_list = alphabet[shift:] + alphabet[:shift]
print(alphabet)
print(shifted_list)
new_list = []
for itr in index_list:
    new_list.append(shifted_list[itr])

print(''.join(new_list))

# encoded = ''.join(shifted_list[itr] for itr in index_list)
# print(encoded)