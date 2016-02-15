from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

sortlist = []

with open(babypath) as f:
	lines = f.readlines()
	# counter = 1
	for line in lines:
		splitLine = line.rstrip('\n').split(',')
		topbabynames = (splitLine[0])
		topbabynum = (splitLine[2])
		# print (counter, ".", topbabynames,topbabynum)
		sortlist.append((topbabynames,topbabynum))

	sortlist.sort(key=lambda data: int(data[1]), reverse=True)
	for x in range(10):
		print (x+1, ('.'), sortlist[x][0],(','), sortlist[x][1])

