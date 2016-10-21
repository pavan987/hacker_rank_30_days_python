
'''
Task
Given a base- integer n, , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive '1s in n's binary representation.
'''

#!/bin/python

import sys

n = int(raw_input().strip())

count = 0
maxcount = 0
while n > 0:
    rem = n % 2
    if rem == 1:
        count += 1
        if count > maxcount:
            maxcount = count
    else:
        count = 0
    n = n / 2
print maxcount

