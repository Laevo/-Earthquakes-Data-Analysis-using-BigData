#!/usr/bin/env python

import sys


for line in sys.stdin:
        line = line.strip()
        lines = line.split("\n")
        for line in lines:
            columns = line.split(",")
            print ("%s\t%d" %(columns[4],1))
