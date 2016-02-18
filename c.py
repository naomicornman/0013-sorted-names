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

for name in namesdict:
		if namesdict[name] >= 2000:
			sortlist.append([name, namesdict[name], len(name)])

orderedlist = sorted(sortlist, key = itemgetter(2,1), reverse = True)
	
for x in range (10):
	print (orderedlist[x][0].ljust(11), str(orderedlist[x][1]).rjust(13),sep = '')


	