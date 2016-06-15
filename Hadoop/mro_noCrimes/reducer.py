#!/usr/bin/env python

from operator import itemgetter
import sys

current_crime = None
current_count = 0

for line in sys.stdin:
        line = line.strip()
        try:
                crime, count = line.split('\t',1)
                count = int(count)
        except:
                continue

        if current_crime == crime:
                current_count += count
        else:
                if current_crime:
                        print ("%s\t%d" %(current_crime,current_count))
                current_crime = crime
                current_count = count

if current_crime == crime:
        print( "%s\t%d" %(current_crime, current_count))
