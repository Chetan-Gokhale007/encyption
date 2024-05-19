import random

def coding():
  word= input("Enter the word for coding: ").lower()
  if(len(word)>=3):
    word = word[1:] + word[0] #remove the first letter and append it at the end
    word = "".join(random.choices("abcdefghijklmnopqrstuvwxyz",k=3)) + word + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=3)) #append three random characters at the starting and       the end
    print(word)
  else:
    word = word[::-1]
    print(word)

def decoding():
  word = input("Enter the word for decoding: ")
  if(len(word)>=3):
    word = word[3:-3] #remove 3 random characters from start and end
    word = word[-1] + word[:-1]  #Now remove the last letter and append it to the beginning
    print(word)
  else:
    word = word[::-1]
    print(word)


print("1. Coding")
print("2. Decoding")
choice = int(input("Enter your choice: "))
if(choice==1):
  coding()
elif(choice==2):
  decoding()
