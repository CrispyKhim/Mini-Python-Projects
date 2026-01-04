import random

wordList = ["python", "hangman", "cat", "multiplication", "thing"]
correctWord = random.choice(wordList)

display = ""
for letter in correctWord:
  display += "-"

print("Welcome to Hangman!")

lives = 10

guessedLetters = [None] * len(correctWord)

while lives > 0:
  print("You have " + str(lives) + " guesses left.")
  print(display)
  guess = input("What is your guess?: ")
  
  if len(guess) == 0:
    print("Please type a letter or word.")
    
  elif len(guess) > 1:
    if guess == correctWord:
      print("You guessed right! The word is indeed " + guess + "!")
      break
    else:
      print("It is not " + guess + ".")
      lives -= 1
  
  else:
    if guess in correctWord:
      print("The word does contain '" + guess + "'!")
    
      display = ""
      for i in range(len(correctWord)):
        if guess == correctWord[i]:
          guessedLetters[i] = guess
          
        if guessedLetters[i] == None:
          display += '-'
        else:
          display += guessedLetters[i]
    
    else: 
      print("There is no '" + guess + "' in this word.")
      lives -= 1