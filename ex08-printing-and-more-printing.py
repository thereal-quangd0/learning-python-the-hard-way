formatter = "%r %r %r %r"

#pulls formatter variable from above, using the formatting string approach, pulls in variables from the right (1, 2, 3, 4)
print formatter % (1, 2, 3, 4)

#prints out strings with single quotes around each item
print formatter % ("one", "two", "three", "four")

#prints out booleans True and False
print formatter % (True, False, False, True)

#prints out 'block' of string, notice that each line has a tab to begin with.
print formatter % (
	"I had this thing.",
	"Second line",
	"3rd line",
	"finale line"
)

# number of items to the right of the percent sign MUST 
# match the number of variables set in the "formatter" variable (4)