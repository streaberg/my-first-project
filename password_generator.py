
import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    """Generate a strong random password."""

    # Base characters
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>/?"

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

import random
import string

def generate_password(length=16, use_upper=True, use_numbers=True, use_symbols=True, exclude_similar=False):
    """Generate a strong random password"""

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

    if exclude_similar:
        uppercase = uppercase.replace("I", "").replace("O", "")
        lowercase = lowercase.replace("l", "").replace("o", "")
        numbers = numbers.replace("0", "").replace("1", "")

    characters = lowercase
    if use_upper:
        characters += uppercase
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Strong Password Generator v2 - Made by Streaberg with Abundance")
    print("=" * 60)

    try:
        length = int(input("Password length (recommended 12-20): "))
        if length < 8:
            length = 12

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        exclude_similar = input("Exclude similar characters (1,l,I,0,O)? (y/n): ").lower() == 'y'

        count = int(input("How many passwords to generate? (1-10): ") or 1)
        if count > 10:
            count = 5

        print("\n" + "="*60)
        print("Generated Passwords:\n")

        with open("generated_passwords.txt", "a") as file:
            for i in range(count):
                pwd = generate_password(length, use_upper, use_numbers, use_symbols, exclude_similar)
                print(f"{i+1}. {pwd}")
                file.write(f"Password {i+1}: {pwd} | Length: {length} | Generated: March 2026\n")

        print("\n All passwords saved to 'generated_passwords.txt'")

    except ValueError:
        print(" Please enter valid numbers.")

if __name__ == "__main__":
    main()
