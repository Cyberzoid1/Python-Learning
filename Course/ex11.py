print "How old are you?",
age = raw_input()
print "How tall are you?"
height = raw_input()
print "Weight",
weight = raw_input()
name = raw_input("What is your name? ")

#print "you are %d old, %d tall and %d heavy." % (age, height, weight)
print "you are %r old, %r tall and %r heavy." % (age, height, weight)

# crashes on anything other than a number or decimal
str1 = input("type a string: ")
print "The string %r raw, %r string" %(str1,str1)
