import string

alphabet = string.ascii_lowercase

while True:

    direction = input("Enter 'encode' to encode a message or 'decode' to decode a message: ")
    text = input("Enter message: ").lower()
    shift = int(input("Enter the shift number: "))

    def encrypt(text, shift):
        encrypted_text = ""
        for char in text:
            if char in alphabet:
                alphabet_index = alphabet.index(char)
                shifted_index = (alphabet_index + shift) % 26
                shifted_char = alphabet[shifted_index]
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(text, shift):
        decrypted_text = ""
        for char in text:
            if char in alphabet:
                alphabet_index = alphabet.index(char)
                shifted_index = (alphabet_index - shift) % 26
                shifted_char = alphabet[shifted_index]
                decrypted_text += shifted_char
            else:
                decrypted_text += char
        return decrypted_text

    if direction == "encode":
        print(encrypt(text, shift))
    elif direction == "decode":
        print(decrypt(text, shift))

    next_action = input("Would you like to play again or quit: ").lower()
    if next_action != "play":
        break


