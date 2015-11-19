# What this app does:
# 1. Asks a question.
# 2. Displays prompt for user to input an answer.
# 3. Stores the answer for a short amount of time.
# 4. System presents back to you your answers

print "Let's get some basic diagnostics."

print "First name?",
fname = raw_input()

print "Age?",
age = raw_input()

print "Height? (American standard)",
height = raw_input()

print "Weight?",
weight = raw_input()

print "Race?",
race = raw_input()

print """
\tNice to meet you %s. Here's your basics:
\t\t* Age: %s
\t\t* Weight: %s
\t\t* Height: %s
\t\t* Race: %s
""" % ( fname, age, weight, height, race)