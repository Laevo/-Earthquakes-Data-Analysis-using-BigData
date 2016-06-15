#!/usr/bin/env python

import sys


for line in sys.stdin:
        line = line.strip()
        tuples = line.split("\n")
        for line in tuples:
            columns = line.split(",")
            crime = columns[4]
            date = columns[1]
            data = date.split("/")
            try: 
                 year = data[2]
                 print ("%s\t%s\t%d" %(crime,year,1))
            except:
                 pass
