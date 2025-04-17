#python Project 03: Guessing the number(User) by Areeba Yaseen:
import random

def computer_guess(x):
    print("\n🎯🔢 WELCOME TO THE GUESSING GAME! 🔢🎯")
    print("🤖 The computer will try to guess your number! Let's see if it can win! 🚀\n")

    low = 1
    high = x
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low > high:
            print("🚨 Something went wrong. Please restart the game! 🔄")
            break

        guess = random.randint(low, high)
        feedback = input(f"🤔 Is {guess} too low (📉 L), too high (📈 H), or correct (✅ C)? ").lower()
        attempts += 1
        print(f"🔢 Attempts: {attempts}")

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"🎉 Yeeh! The computer guessed your number {guess} correctly in  {attempts} attempts! 🏆🎊")
            break

        if attempts == 5:
            print("❌ Game Over! Your number of attempts exceeded. You lose the game. 😞💔")
            break


computer_guess(10)
