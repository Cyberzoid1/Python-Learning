from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy %s to %s" %(from_file, to_file)

#we could do these two in one line. how?
in_file = open(from_file)
indata = in_file.read()

print "The in file is %d bytes" % len(indata)

print "Does out file exist %r" % exists(to_file)
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "done"
out_file.close()
in_file.close()
