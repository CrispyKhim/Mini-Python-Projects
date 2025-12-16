import random

def sort(msg):
  wordList = msg.split(' ')
  
  result = ""
  
  for word in wordList:
    arr = list(word)
    arr.sort()
    for letter in arr:
      result += letter
    result += " "
    
  return result;

def reverse(msg):
  result = ""
  
  for letter in reversed(msg):
    result += letter
    
  return result

def shuffleMsg(msg):
  result = ""
  
  wordList = msg.split(' ')
  
  for word in wordList:
    arr = list(word)
    random.shuffle(arr)
    for letter in arr:
      result += letter
    result += " "
  
  return result

message = input("Write your message here: ")

option =\
  input("Do you want to sort, reverse or shuffle the message? ")

if (option == "sort"):
  encrypt = sort
if (option == "reverse"):
  encrypt = reverse
else:
  encrypt = shuffleMsg

print encrypt(message)

answer = input("Guess the message: ")
if (answer == message):
  print("You win")
else:
  print("You lose")