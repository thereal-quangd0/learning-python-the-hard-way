#imports -- adding features to your application
from sys import argv

# "unpacks" argv from line 2
script, userName = argv
prompt = '> '

print "Hello I'm, %s, the script called %s" % (userName, script)
print "I'd like to ask you a few questions. Have a seat."
print "Do you like me, %s with %s." % (userName, script)
like = raw_input(prompt)

print "Where do you live %s" % userName
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alight, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have an %r computer. Nioce.
""" % (like, lives, computer)