import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_words():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words) 
        
    return word.upper()  

def hangman():
    print("🎉 Welcome to the Hangman Game! 🎉\n")
    print("🔠 Try to guess the word, one letter at a time!\n")
    
    word = get_words()
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7  

    while len(word_letters) > 0 and lives > 0:
        print(f"\n❤️ Lives Left: {lives} | 🔡 Used Letters: {' '.join(sorted(used_letters)) or 'None'}")

        # Display the hangman visual
        print(lives_visual_dict[lives])

        # Show the current word progress
        word_list = [letter if letter in used_letters else '⬜' for letter in word]
        print("📝 Current Word:", ' '.join(word_list))

        # Take user input
        user_letter = input("\n✏️ Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Good job! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"❌ Oops! '{user_letter}' is not in the word. You lost a life.")

        elif user_letter in used_letters:
            print("⚠️ You've already guessed that letter! Try a new one.")     

        else:
            print("🚫 Invalid input! Please enter a valid letter.")     

    # Game Over 
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"💀 Game Over! You ran out of lives. The word was: **{word}**")
    else:
        print(f"🎉 Congratulations! You guessed the word: **{word}** 🎊")

if __name__ == "__main__":
    hangman()
