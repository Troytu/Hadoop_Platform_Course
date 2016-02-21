#!/usr/bin/env python
import sys

previous = ''
sum = 0
line_count = 0
has_abc = False
for line in sys.stdin:
    # Same logic from wordcount
    line_count += 1
    line = line.strip()
    key_value = line.split('\t')
    key = key_value[0]
    value = key_value[1]
    # If previous differs from actual key, means that key is updated. we need to print the previous values.
    if key != previous:
        if line_count > 1 and has_abc:
            print ('{0}\t{1}'.format(previous, sum))
        sum = 0
        previous = key
        has_abc = False

    if value == 'ABC':
        has_abc = True
    elif value.isdigit():
        sum += int(value)

if has_abc:
    print ('{0} \t {1}'.format(previous, sum))