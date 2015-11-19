#imports -- adding features to your application
from sys import argv

#unpacks argv from line 2
script, first, second, third = argv

# Study Drills
scriptName = raw_input("Name of Script, por favor? : ")
firstArg = raw_input("Your first argument, madam. : ")
secondArg = raw_input("And your second argument? : ")
thirdArg = raw_input("Lastly, your turd... : ")

print "The script is called: %s" % (scriptName)
print "Your 1st variable is: %s" % (firstArg)
print "Your 2nd variable is: %s" % (secondArg)
print "Your 3rd variable is: %s" % (thirdArg)
