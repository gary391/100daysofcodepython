
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
"""
shift = 5

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']
"""
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    ## Method 1

    end_text = ""
    if (direction == 'decode'):
        shift = shift * -1
    for letter in text:
        position = alphabet.index(letter)
        print(f"Existing position: {position}")
        new_position = position + shift

        print(f"What is shift: {shift}")
        print(f"What is the new_position: {new_position}")
        end_text = end_text + alphabet[new_position]
    print(f"The {direction} text is {end_text}")



    ## Method 2

    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    #             'v', 'w', 'x', 'y', 'z']
    # shifted_list = alphabet[shift:] + alphabet[:shift]
    # new_list = []
    # if(direction == "decode"):
    #     shifted_list, alphabet = alphabet, shifted_list
    #
    # for char in text:
    #     if char in alphabet:
    #         index = alphabet.index(char)
    #         new_char = shifted_list[index]
    #         new_list.append(new_char)
    #     else:
    #         print("When will this line of code gets executed!!!")
    #         new_list.append(char)
    # result = "".join(new_list)
    # print(f"The {direction} text is {result}")

    ## Method 3

    # for i in text:
    #     for index, item in enumerate(alphabet):
    #         if (item == i):
    #             index_list.append(index)
    # for itr in index_list:
    #     new_list.append(shifted_list[itr])
    # if(direction == 'decode'):
    #     shifted_list, alphabet = alphabet, shifted_list
    #
    #     for i in text:
    #         for index, item in enumerate(shifted_list):
    #             if (item == i):
    #                 index_list.append(index)
    #
    #     for itr in index_list:
    #         new_list.append(alphabet[itr])
    #
    # print(f" The {direction} text is {''.join(new_list)}")

caesar(text=text, shift=shift, direction=direction)