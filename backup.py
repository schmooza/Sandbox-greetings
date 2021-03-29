#main.py

from myCode import *

# this is the basic function
doSomething()



# this is a bit harder. 
# Don't worrry, you don't need to know this.
# The basic idea is that we can pass data around, like the tape on the string activity. 


name = input("What is your name? \nType your name here: ")
print("")
nameIs = doSomethingHelloMessage(name)

age = input("How old are you? \nType your age here: ")
print("")
doSomethingAdd(nameIs, age)


#-----------------------------------------------

# myCode.py
def doSomething():
	print("I made this code.")



def doSomethingHelloMessage(name):
  print(f"Hi there {name}.")
  return name


def doSomethingAdd(name, age):
  print(f"Wow {name} are you really {age}?")