#!/usr/bin/env python

from operator import itemgetter
import sys

current_crime = None
current_year = None
current_count = 0

for line in sys.stdin:
        line = line.strip()
        try:
                line = line.split('\t')
                crime = line[0]
                year = line[1]
                count = line[2]
                count = int(count)
        except:
                continue

        if current_crime == crime and current_year == year:
                current_count += count
        else:
                if current_crime and current_year:
                        print ("%s\t%s\t%d" %(current_crime, current_year,current_count))
                current_crime = crime
                current_year = year
                current_count = count

if current_crime == crime and current_year == year:
        print( "%s\t%s\t%d" %(current_crime, current_year, current_count))
