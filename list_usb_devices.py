import os
import time
import re

devices = os.popen('sudo blkid').readlines()

usbs = []
for u in devices:
    loc = [u.split(':')[0]]
    if '/dev/sd' not in loc[0]:
        continue  # skip
    loc += re.findall(r'"[^"]+"', u)
    columns = ['loc']+re.findall(r'\b(\w+)=', u)

    usbs.append(dict(zip(columns, loc)))

for u in usbs:
    print('Device %(LABEL)s is located at $(loc)s with UUID of $(UUID)s' % u)
