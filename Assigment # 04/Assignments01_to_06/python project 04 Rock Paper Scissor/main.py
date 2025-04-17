#Python Project 04: Rock , Paper and Scissor by Areeba Yaseen
import random

print("\n🎉 WELCOME TO THE ROCK, PAPER, SCISSORS GAME! 🎉")
print("\n🔥 It's a best-of-3 game! The first to win 2 rounds will be the champion! 🏆")

#function for the game
def play_Game():
    user_score = 0
    computer_score = 0
    rounds = 3 # 3 rounds game


    for i in range(rounds):
        print(f"\n🎮 Round {i+1}")
        user = input("Enter Your choice: 'r' for Rock, 'p' for Paper, 's' for Scissor: ").lower()
        computer = random.choice(["r", "s", "p"])

        print(f"🖥️ Computer chose: {computer}")

        if user == computer:
            print("🤝 It's a tie!!!")
        elif is_win(user, computer):
            print("✅ You won this round!")
            user_score += 1
        else:
            print("❌ Computer won this round!")
            computer_score += 1

        print(f"📊 Score: You {user_score} - {computer_score} Computer")

        # Agar koi 2 jeet jaye, game khatam
        if user_score == 2 or computer_score == 2:
            break

    print("\n🏆 FINAL RESULT 🏆")
    if user_score > computer_score:
        print("🎉 Congratulations! You won the game! 🎉")
    else:
        print("😢 Oh no! Computer won the game!")

def is_win(player, opponent):
    return (player == "r" and opponent == "s") or \
           (player == "s" and opponent == "p") or \
           (player == "p" and opponent == "r")

play_Game()  # Start the game
