from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

sortlist = []

with open(babypath) as f:
	lines = f.readlines()
	for line in lines:
		splitLine = line.rstrip('\n').split(',')
		topbabynames = (splitLine[0])
		topbabynum = (splitLine[2])
		sortlist.append((topbabynames,topbabynum))

	counter = 0

	sortlist.sort(key=lambda data: len(data[0]), reverse=True)
	for x in sortlist:
		if int(x[1]) > 2000: 
			if counter <= 9: 
				counter = counter + 1
				print (x[0].ljust(15), x[1].rjust(10)) 

		