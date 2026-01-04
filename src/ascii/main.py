def print_ascii():
  for i in range(32,256):
    print(str(i) + " = " + chr(i))

def asciify_message(message):
  result = ""
  
  for letter in message:
    result += str(ord(letter)) + " "
  
  return result

def deasciify_message(message):
  result = ""
  
  message = message.split()
  for number in message:
    result += chr(int(number))

  return result

answer = input("Encrypt[e] or Decrypt [d]? ")

if answer == "e":
  option = asciify_message
elif answer == "d":
  option = deasciify_message
  
print(option(input("Write your message here: ")))