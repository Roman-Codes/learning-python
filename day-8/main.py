from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(word, shift_value, direction):
    end_text = ''
    if direction == 'decode':
        shift_value *= -1
    for char in word:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_value
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(end_text)

run_again = 'yes'

while run_again == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    run_again = input("Go again?\n")
    caesar(word=text, shift_value=shift, direction=direction)
else: 
    print('bye!')
