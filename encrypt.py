def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char)- shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    plain_text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted = caesar_cipher(plain_text, shift)
    print("Encrypted text: (encrypted)")

    # Save to file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)