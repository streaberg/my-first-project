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

    return password

def main():
    print(" Strong Password Generator by Streaberg ")
    print("=" * 50)

    try:
        length = int(input("How long should the password be? (minimum 8): "))
        if length < 8:
            length = 8
            print("Using minimum length of 8 characters.")

        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_upper, use_numbers, use_symbols)

        print("\n Your strong password is:")
        print(password)

        # Save to file
        with open("generated_passwords.txt", "a") as file:
            file.write(f"Password: {password} | Length: {length} | Date: March 2026\n")

        print("\n Password saved to 'generated_passwords.txt'")

    except ValueError:
        print(" Please enter a valid number for length.")

if __name__ == "__main__":
    main()
