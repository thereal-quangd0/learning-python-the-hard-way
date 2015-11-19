# What this app does:
# 1. Asks a question.
# 2. Displays prompt for user to input an answer.
# 3. Stores the answer for a short amount of time.
# 4. System presents back to you your answers

print "Let's get some basic diagnostics."

fname = raw_input("First name?")
age = raw_input("Age?")
height = raw_input("Height? (American standard)")
weight = raw_input("Weight?")
race = raw_input("Race?")

print """
\tNice to meet you %s. Here's your basics:
\t\t* Age: %s
\t\t* Weight: %s
\t\t* Height: %s
\t\t* Race: %s
""" % ( fname, age, weight, height, race)