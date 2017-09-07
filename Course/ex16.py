from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "continue?"
raw_input("?")

print "Opening"
target = open(filename, 'w')

print "Truncating"
target.truncate()

print "asking for 3 lines"
line1 = raw_input("line 1: ")
line2  = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "writing"


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("------------\n")
#single method
formatter = "%r\n%r\n%r\n"
mystr = formatter % (line1, line2, line3)
target.write(mystr)
target.write("------------\n")

#concatination
mystr2 = line1 + " " + line2 + " " + line3 + "\n"
target.write(mystr2)

print "closing"
target.close()
