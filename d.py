from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

m_dict = {}
f_dict = {}

counter = 0

print ("Female")

with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			if 'x' in name or "X" in name:
				if counter <= 4:
					counter = counter + 1
					print (counter, ".", name.ljust(15), babies.rjust(8))


print ("Male")

counter=0
with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if sex == 'M':
			if 'x' in name or "X" in name:
				if counter <= 4:
					counter = counter + 1
					print (counter, name.ljust(15), babies.rjust(8))



