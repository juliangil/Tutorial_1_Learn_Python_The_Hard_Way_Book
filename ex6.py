x = "There are %d types of people." % 10
#start a variable of string type

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) 
#two put inside a string

print x
print y

print "I said: %r." % x
#percent r (%r) repet the line of the variable x but with one variation
print "I also said: '%s'." % y
#two put inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
#the plus or + is a concanetation