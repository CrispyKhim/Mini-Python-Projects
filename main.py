morseDictionary = {
  "a" : "-----",
  "b" : ".----",
  "c" : "..---",
  "d" : "-..",
  "e" : ".",
  "f" : "..-.",
  "g" : "--.",
  "h" : "--.",
  "i" : "..",
  "j" : ".---",
  "k" : "-.-",
  "l" : ".-..",
  "m" : "--",
  "n" : "-.",
  "o" : "---",
  "p" : ".--.",
  "q" : "--.-",
  "r" : ".-.",
  "s" : "...",
  "t" : "-",
  "u" : "..-",
  "v" : "...-",
  "w" : ".--",
  "x" : "-..-",
  "y" : "-.--",
  "z" : "--..",
  "0" : "-----",
  "1" : ".----",
  "2" : "..---",
  "3" : "...--",
  "4" : "....-",
  "5" : ".....",
  "6" : "-....",
  "7" : "--...",
  "8" : "---..",
  "9" : "----.",
  " " : "/"
}

def encrypt(message):
  result = ""
  
  for letter in message:
    if letter in morseDictionary:
      result += morseDictionary[letter] + " "
  
  return result

print "Welcome to your very own Morse Coder."
print "\n***\n"

while True:
  print "Mesage to be sent: " + encrypt(input("Enter your message here: "))
  print ""
  
  if input("Do you want stop? (y/n)") == "y":
    print "\n***\n"
    print "Goodbye!"
    break
  print ""