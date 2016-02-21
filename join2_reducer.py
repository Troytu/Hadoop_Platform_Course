#!/usr/bin/env python
import sys

previous = ''
sum = 0
line_count = 0
for line in sys.stdin:
    # Same logic from wordcount
    line_count += 1
    line = line.strip()
    key_value = line.split('\t')
    key = key_value[0]
    value = key_value[1]
    # If previous differs from actual key, means that key is updated. we need to print the previous values.
    if key != previous:
        if line_count > 1:
            print ('{0}\t{1}'.format(previous, sum))
            sum = 0
        previous = key
    # I guess this was useful, but not
    # if value == 'ABC':
    #     sum += 1
    if value.isdigit():
        sum += int(value)

print ('{0} \t {1}'.format(previous, sum))