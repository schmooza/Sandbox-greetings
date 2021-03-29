from myCode import *
from colored import fg, bg, attr


# this is the basic function
doSomething()



# Below is a bit harder. 
# Don't worrry, you don't need to know this.
# The basic idea is that we can share data, like the tape on the string activity. 

# fancy code to add colors, it looks like a mess of symbols. 
name = input("%s%s What is your name? \nType your name here: %s" % (fg('black'), bg('yellow'), attr('reset')))

print("######################")
nameIs = doSomethingHelloMessage(name)

age = input("How old are you? \nType your age here: ")
print("")


doSomethingAdd(nameIs, age)