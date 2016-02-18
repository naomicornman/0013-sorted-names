from os.path import basename, join
from operator import itemgetter

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

sortlist = []
namesdict = {}
with open(babypath) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        if namesdict.get(name):
            namesdict[name] += int(babies)
        else:
            namesdict[name] = int(babies)

# with open(babypath) as f:
# 	lines = f.readlines()
for name in namesdict:
		if namesdict[name] >= 2000:
			sortlist.append([name, namesdict[name], len(name)])
	# for line in lines:
	# 	splitLine = line.rstrip('\n').split(',')
	# 	topbabynames = (splitLine[0])
	# 	topbabynum = (splitLine[2])
	# 	sortlist.append((topbabynames, topbabynum))

	# counter = 0

orderedlist = sorted(sortlist, key = itemgetter(2,1), reverse = True)
	# sortlist.sort(key=lambda data: len(data[0]), reverse=True)
for x in range (10):
	# for x in sortlist:
	# 	if int(x[1]) > 2000: 
	# 		if counter <= 9: 
	# 			counter = counter + 1
	print (orderedlist[x][0].ljust(11), str(orderedlist[x][1]).rjust(13),sep = '')
	# print (orderedlist[x][0].ljust(15), str(orderedlist[x][1].rjust(10))) 

	