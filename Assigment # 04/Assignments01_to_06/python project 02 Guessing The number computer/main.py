#Python Project 02: Guessing the random number (Computer) by Areeba Yaseen

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0

    print("🎯 Welcome to the Guessing Number Game! 🎯")
    print("🔢 You have 5 attempt limits! Try your best. 💪")



    while guess != random_number:

        guess = int(input(f"\n🤔 Guess a number between 1 and {x}: "))
        attempts += 1
        print(f"\r📝 Attempts: {attempts}")


        if guess > random_number:
            print("\n📈 Too high! Try again. ⬆")
        elif guess < random_number:
            print("\n📉 Too low! Try again. ⬇")
        else:
            print(f"\n🎉 Congratulations! You guessed it right in {attempts} attempts! 🏆")
            break

        if attempts == 5:
            print("\n💀 Game Over! Your attempt limit has exceeded. Try again next time! ❌")
            break

guess(10)
