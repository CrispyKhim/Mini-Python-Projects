import random

listOfChars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

noOfPasswords = input("How many passwords do you want? ")

passwordType = input('''
Select your type of password:
- any combination
- lower case only
- CAPS only
Write your option below: 
''')

if passwordType == "lower case only":
  listOfChars = listOfChars[0:26]
if passwordType == "CAPS only":
  listOfChars = listOfChars[26:52]

for j in range(int(noOfPasswords)):
  password = ""
  
  for i in range(26):
    password += listOfChars[random.randint(0,len(listOfChars)-1)]
  
  print(password)