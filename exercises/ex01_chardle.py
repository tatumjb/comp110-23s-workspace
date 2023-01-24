"""EX01 - Chardle"""

__author__ = "730467683"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
 print("Error: Word must contain 5 characters")
 exit()

letter: str = input("Enter a single character: ")

if len(letter) != 1:
 print("Error: Character must be a single character.")
 exit()

counter: int = 0 

print("Searching for " + letter + " in " + word)
if word[0] == letter:
 counter += 1 
 print(letter + " found at index 0")

if word[1] == letter:
 counter += 1 
 print(letter +" found at index 1")

if word[2] == letter:
 counter += 1 
 print(letter + " found at index 2")

if word[3] == letter:
 counter += 1 
 print(letter + " found at index 3")

if word[4] == letter:
 counter +=1
 print(letter +" found at index 4")

if counter == 0:
 print("No instances of " + letter + " found in " + word)

if counter == 1:
 print("1 instance of " + letter + " found in " + word)

if counter == 2:
 print("2 instances of " + letter + " found in " + word)

if counter == 3:
  print("3 instances of " + letter + " found in " + word)

if counter == 4:
 print("4 instances of " + letter + " found in " + word)

if counter == 5:
 print("5 instances of " + letter + " found in " + word)
 


