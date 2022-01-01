"""
# -*- coding: utf-8 -*-
@Created on 12:46 2022-01-01

@Describe:
weblink for this puzzle:
https://adventofcode.com/2021/day/3

@author: TK
"""
import urllib.request

#from urllib.request import urlopen

def powerConsumption(file):
    with open(file, 'r') as f:
        #print(f.readline())
        count = [0 for i in range(len(f.readline().strip()))]
        #print(len(f.readline()))
        gamma = ['0' for i in range(len(f.readline().strip()))]
        epsilon = ['0' for i in range(len(f.readline().strip()))]
        f.seek(0)
        length = len(f.readlines())
        f.seek(0)
        for x in f.readlines():
            for i in range(len(x.strip())):
                if x[i] == '1':
                    count[i] += 1
    for i in range(len(count)):
        if count[i] > length/2:
            gamma[i] = '1'
            #print(i)
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'
    #print(gamma)
    #print(epsilon)
    gamma = int(''.join(gamma),2)
    epsilon = int(''.join(epsilon), 2)
    #print(count)
    #print(length)
    #print(gamma)
    #print(epsilon)
    return (gamma*epsilon)

#def webop(url):
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#    req = urllib.request(url=url, headers=headers)
#    x = urllib.request.urlopen(req).readlines()
#    print(len(x))


if __name__ == '__main__':
    print(powerConsumption('..\\files\\Day 3 data.txt'))
    #webop("https://adventofcode.com/2021/day/3/input")
    #webop('https://www.google.com')