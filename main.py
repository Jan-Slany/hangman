import random

# seznam slov
guesing_word = [
"pizza", "emergency", "check", "descent", 
"cancel", "snub", "dump", "army", 
"grandmother", "family", "slap", "transmission",
"stereotype", "plant", "shelf", "obese", 
"lunch", "fill", "hesitate", "difficulty", 
"borrow", "deliver", "jail", "control", 
"team", "chaos", "experiment", "bean", 
"be", "challenge", "tease", "excavate", 
"matrix", "enter", "compromise", "pasture", 
"movement", "stride", "disappear", "constituency", 
"diameter", "bring", "ostracize", "confront", 
"reproduction", "interest", "technique", "dome", 
"aspect", "lick", "oppose", "house"]

random_word = random.choice(guesing_word)

word_char = []
underscores_word = []

hangman_index = 0
hangman = [
'''






=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  X   |
 /|\\  |
 / \\  |
      |
=========''']

for item in random_word:
	word_char.append(item)
	underscores_word.append("_")

# hangman text
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
 ___________.._________/ |                      
| .__________))_________/   
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (/ `_.'  -created by Jan Slaný

''')

while True:
  for item in underscores_word:
    print(item, end=" ")
  user_input = input("\nZadej písmeno: ")

  if user_input in word_char:
    print("You'r guess was correct "+ str(user_input) +" is in the word!\n")
    index = word_char.index(user_input)
    
    underscores_word[index] = user_input

    if user_input is word_char[-1]:
      pass

    elif user_input in word_char[index+1]:
      underscores_word[index+1] = user_input

    elif underscores_word == word_char:
      print("You won, the word was:"+ str(random_word))
      break
      
  else:
    print(str(user_input)+" Wasn't in the list! \n")
    print(hangman[hangman_index])
    hangman_index += 1

    if hangman_index == 8:
      print("You have lost! The word was: "+str(random_word))
      break
