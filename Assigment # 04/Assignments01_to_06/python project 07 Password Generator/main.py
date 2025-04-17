import random

def generate_password(length):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    special = "&?!@#$%^*"

    # Ensure at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = lower + upper + digits + special

    # Fill remaining length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to randomize placement of characters
    random.shuffle(password)

    return "".join(password)

def main():
    print("🔐 Welcome to the Strong Password Generator! 🔐")

    number = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter your password length (min 4): "))

    if password_length < 4:
        print("❌ Password length should be at least 4 characters.")
        return

    print(f"\n📝 Here are your {number} strong passwords:")


#loop to print the password for the user defined number of times
    for _ in range(number):
        print(generate_password(password_length))

main()
