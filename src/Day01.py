# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:46:07 2021
weblink for the puzzle:
https://adventofcode.com/2021/day/1

count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

all data are stored in txt file: sonar sweep data.txt

@author: TK
"""

def FindLargerNum(file):
    temp = -1
    count = 0
    with open(file, 'r') as f:
        for x in f.readlines():
            if temp != -1 and int(x) > temp:
                count += 1
            temp = int(x)
    return count

if __name__ == '__main__':
    print(FindLargerNum('..\\files\Sonar Sweep data.txt'))
