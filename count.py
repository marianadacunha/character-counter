import pprint

print("Type your text below.")
userInput = input()

count = {}

for character in userInput.lower():
    count.setdefault(character, 0)
    count[character] += 1

print(f"Your text has the following letters, the following number of times:")
pprint.pprint(count)