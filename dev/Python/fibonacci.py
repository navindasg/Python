import sys
if len(sys.argv) < 2:
	print "You must enter an integer argument!"
else:
	x = 1
	tmp = 0
	for i in range(int(sys.argv[1])):

		print x
		tmp1 = x
		x = x + tmp
		tmp = tmp1

