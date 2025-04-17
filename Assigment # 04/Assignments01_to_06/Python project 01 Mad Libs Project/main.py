# Python Project 01: "The Magical Jungle Adventure" - Mad Libs by Areeba Yaseen

# User input
name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
place = input("Enter a mysterious place: ")
adjective2 = input("Enter another adjective: ")
creature = input("Enter a mythical creature: ")
object1 = input("Enter an object name: ")
verb = input("Enter an action / verb: ")
object2 = input("Enter a magical object: ")
sound = input("Enter a funny or scary sound: ")
superpower = input("Enter a superpower: ")

# Predefined template
madLib_story = f"""
Once upon a time, the fearless explorer **{name}** set out on a journey to the **{adjective1} land of {place}**. 🌎✨
Legends said that deep inside the {place}, a secret treasure was hidden, guarded by an ancient {creature}! 😨

As {name} walked through the dense jungle, the air grew **{adjective2}**, and suddenly...
**"{sound}!"** echoed from the shadows! Out of nowhere, a **{creature}** appeared, its eyes glowing! 👀

Without thinking, {name} grabbed a **{object1}** and started to **{verb}**, hoping to scare it away.
But instead of attacking, the {creature} **started laughing!** 🤣

"You’re funny, {name}!" it said. "But you must prove yourself worthy!"
The creature handed {name} a **magical {object2}** and whispered,
_"This holds the key to your destiny. But beware… the jungle is watching."_ 🌙🌿

Before {name} could ask anything, **POOF!** The {creature} vanished! 😱
The magical {object2} started **glowing**, and suddenly...
**{name} discovered they had gained the power of {superpower}!** 🔥🦸‍♂️

What happens next? Will {name} uncover the jungle’s secret? Or face even greater danger?
Only time will tell... 😏
"""

# Printing the story
print("\n✨ Here is your crazy adventure Mad Libs story:\n")
print(madLib_story)
