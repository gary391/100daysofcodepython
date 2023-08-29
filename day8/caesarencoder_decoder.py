alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
"""
shift = 5

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']
"""
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    # Get the current indices of all the word

    index_list = []
    for i in plain_text:
        for index, item in enumerate(alphabet):
            if (item == i):
                index_list.append(index)
    # print(index_list)

    shifted_list = alphabet[shift:] + alphabet[:shift]
    # print(alphabet)
    # print(shifted_list)
    new_list = []
    for itr in index_list:
        new_list.append(shifted_list[itr])

    print(f" The encoded text is {''.join(new_list)}")

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def decrypt(plain_text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    # Get the current indices of all the word
    shifted_list = alphabet[shift:] + alphabet[:shift]
    index_list = []
    for i in plain_text:
        for index, item in enumerate(shifted_list):
            if (item == i):
                index_list.append(index)
    # print(index_list)


    # print(alphabet)
    # print(shifted_list)
    new_list = []
    for itr in index_list:
        new_list.append(alphabet[itr])

    print(f" The decoded text is {''.join(new_list)}")


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

if(direction == 'encode'):
    encrypt(plain_text=text, shift=shift)
else:
    decrypt(plain_text=text, shift=shift)
