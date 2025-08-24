# Secret Code Generator using Caesar Cipher
# Author: Vidhyadharshinie
# This program encodes and decodes messages by shifting letters in the alphabet.

# ------------------------- FUNCTION DEFINITIONS -------------------------

def encode_message(message, shift):
    """
    Encodes the given message by shifting each letter forward
    according to the Caesar Cipher logic.
    Non-alphabet characters (spaces, punctuation) are left unchanged.
    """
    result = ""
    for char in message:
        if char.isalpha():  # Check if character is a letter
            # ASCII value for 'A' = 65, 'a' = 97
            base = ord('A') if char.isupper() else ord('a')
            # Shift within the range of 26 letters
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-letters as is
    return result


def decode_message(message, shift):
    """
    Decodes the given message by shifting each letter backward.
    Decoding is just encoding with negative shift.
    """
    return encode_message(message, -shift)


def menu():
    """
    Displays the main menu and allows the user to choose between:
    1. Encode a message
    2. Decode a message
    3. Exit
    """
    while True:
        print("\n--- Secret Code Generator ---")
        print("1. Encode a Message")
        print("2. Decode a Message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            text = input("Enter the message to encode: ")
            shift = int(input("Enter the shift number: "))
            encoded = encode_message(text, shift)
            print("Encoded Message:", encoded)

        elif choice == "2":
            text = input("Enter the message to decode: ")
            shift = int(input("Enter the shift number: "))
            decoded = decode_message(text, shift)
            print("Decoded Message:", decoded)

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# ------------------------- MAIN PROGRAM -------------------------
menu()
