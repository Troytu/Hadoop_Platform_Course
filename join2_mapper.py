#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    key_value = line.split(',')
    key = key_value[0]
    value = key_value[1]
    print('{0}\t{1}'.format(key, value))


