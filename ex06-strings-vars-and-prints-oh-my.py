# variables
sumVar = "There's like.. about %d types of people at this part." % 10
binary = "binary"
doNot = "don't"
daPhrase = "Those who know %s and those who %s" % (binary, doNot)

# words
print sumVar
print daPhrase

print "I said: %r." % sumVar
print "I also said: '%s'." % daPhrase

#more variables
dwightSays = False
jimSays = 'Bears eat beats. %r'

print jimSays % dwightSays

westSide = "This is to the left..."
eastSide = "of this string... And this is to the right..."

print westSide + eastSide