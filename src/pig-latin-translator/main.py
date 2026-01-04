print("Welcome to the Pig Latin Translator!")

vowels =["a", "e", "i", "o", "u"]


while True:
  print("---")
  message = input("Write your secret message here: ")
  
  message = message.split()
  
  secretMessage = ""
  for word in message:
    if word[0] in vowels:
      word += "way"
    else:
      word = word[1:len(word)] + word[0] + "ay"
    secretMessage += word + " "
  
  print("Piglation: " + secretMessage)
  
  answer = input("Do you want another piglation (y/n)?")
  
  if answer == "n":
    print("Oodbyegay")
    break;