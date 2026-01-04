key = 1

def caesarEncrypt(message, key):
  result = ""
  for letter in message:
    letterID = ord(letter)
    letterID += key
    letterID = (letterID - 32) % (127 - 32)
    
    result += chr(letterID + 32)
  return result

def caesarDecrypt(message, key):
  return caesarEncrypt(message, -key)

print(caesarEncrypt("helloz ~", key))
print(caesarDecrypt("ifmmp{! ", key))