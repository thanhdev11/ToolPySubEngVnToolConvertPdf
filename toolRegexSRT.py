from itertools import groupby
from collections import namedtuple

# "chunk" our input file, delimited by blank lines
with open(filename) as f:
    res = [list(g) for b,g in groupby(f, lambda x: bool(x.strip())) if b]


Subtitle = namedtuple('Subtitle', 'number start end content')

subs = []

for sub in res:
    if len(sub) >= 3: # not strictly necessary, but better safe than sorry
        sub = [x.strip() for x in sub]
        number, start_end, *content = sub # py3 syntax
        start, end = start_end.split(' --> ')
        subs.append(Subtitle(number, start, end, content))

'''
subs
Out[65]: 
[Subtitle(number='1', start='00:02:17,440', end='00:02:20,375', content=["Senator, we're making", 'our final approach into Coruscant.']),
 Subtitle(number='2', start='00:02:20,476', end='00:02:22,501', content=['Very good, Lieutenant.'])]
'''