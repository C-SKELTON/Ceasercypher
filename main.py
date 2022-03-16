import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)





play_game = True

while play_game:
    newtext = ""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ")
    message = input("Type your message: ")
    shift = int(input("Type the shift number "))
    if direction == 'decode':
        shift = shift * -1
    for letters in message:
        #print(letters)
        x = alphabet.index(letters)
        x += shift
        newtext += alphabet[x]
    print(f"Here's the {direction}d result: {newtext}")
    if input("Type 'yes' if you want to go again. Otherwise type 'no' ") == 'no':
        print("Goodbye")
        play_game = False

