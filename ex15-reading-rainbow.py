#imports -- adding features to your application
from sys import argv

# "unpacks" argv from line 2
script, filename = argv

#assigns file to the variable "txt"
txt = open(filename)

#spits out the contents of the file in question
print "Here's your shitty file %r:" % filename
print txt.read()

#asks you to re-type the file name, and opens it again... for some reason.
print "Type the filemame again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
