from os import makedirs
from os.path import basename, join

import requests
DATADIR = 'tempdata'
makedirs(DATADIR, exist_ok=True)

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

data = requests.get(URL).text

babynames = open(babypath, 'w')
babynames.write(data)
babynames.close()

print("There are", len(data), 'characters in', babypath) 