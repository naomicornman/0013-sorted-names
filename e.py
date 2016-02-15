from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

totalbabies = 0
with open(babypath) as f:
	for line in f:
		totalbabies += int(line.split(',')[2])

sortlist = []

with open(babypath) as f:
	lines = f.readlines()
	for line in lines:
		splitLine = line.rstrip('\n').split(',')
		topbabynames = (splitLine[0])
		topbabynum = (splitLine[2])
		sortlist.append((topbabynames,topbabynum))

	sortlist.sort(key=lambda data: int(data[1]), reverse=True)
	total = 0 
	for x in range(10):
		total += (int(sortlist[x][1]))
	print ("Names 1 to 10:", "{0:.1f}".format((total/totalbabies) * 100))

	total = 0 
	for x in range (9,100):  
		total += (int(sortlist[x][1]))
	print ("Names 11 to 100:", "{0:.1f}".format((total/totalbabies) * 100))
 
	total = 0 
	for x in range (99,1000):  
		total += (int(sortlist[x][1]))
	print ("Names 101 to 1000:", "{0:.1f}".format((total/totalbabies) * 100))

	total = 0 
	for x in range (1001,9999):  
		total += (int(sortlist[x][1]))
	print ("Names 1001 to 10000:", "{0:.1f}".format((total/totalbabies) * 100))

	total = 0 
	for x in range (9999,30579):  
		total += (int(sortlist[x][1]))
	print ("Names 10001 to 30579:", "{0:.1f}".format((total/totalbabies) * 100))
