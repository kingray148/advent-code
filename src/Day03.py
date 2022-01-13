"""
# -*- coding: utf-8 -*-
@Created on 12:46 2022-01-01

@Describe:
weblink for this puzzle:
https://adventofcode.com/2021/day/3

@author: TK
"""
#import urllib.request

#from urllib.request import urlopen
import numpy as np

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

def lifeSupportRating(file):
    with open(file, 'r') as f:
        input = f.readlines()
    columns = len(input[0].strip())
    rows = len(input)
    input = list(''.join(''.join(input).split('\n')))
    input = np.reshape(input, (rows,columns))   #将数据转换为二维数组以便计算
    #print(input)
    #print(rows)
    #print(columns)
    oxygenRating = input.copy()     #复制input数据进行下一步计算
    co2Rating = input.copy()
    for i in range(0, columns):
        if len(oxygenRating[oxygenRating[:,i]=='1']) >= len(oxygenRating[oxygenRating[:,i]=='0']):  #找出数组某一列钟哪个元素数量较多，保留较多数元素的行
            oxygenRating = oxygenRating[oxygenRating[:,i]=='1']
        else:
            oxygenRating = oxygenRating[oxygenRating[:,i]=='0']
        #oxygenRating = input[input[:,i]==1] if len(input[input[:,i]==1]) >= len(input[input[:,i]==0]) else input[input[:,i]==0]
        if len(oxygenRating) == 1:  #如果剩余数据只有一行，则停止循环返回结果
            break
    for i in range(0, columns):
        if len(co2Rating[co2Rating[:,i]=='1']) >= len(co2Rating[co2Rating[:,i]=='0']) and len(co2Rating[co2Rating[:,i]=='0']) != 0: #找出数组某一列钟元素数量较少，如果较少元素个数不为零则保留较少元素所在行，否则保留个数较多的元素所在行
            co2Rating = co2Rating[co2Rating[:,i]=='0']
        elif len(co2Rating[co2Rating[:,i]=='1']) !=0 :  #与上同理，较少元素行数不为零时取较少元素所在行，否则保留较多元素的行
            co2Rating = co2Rating[co2Rating[:,i]=='1']
        else:
            co2Rating = co2Rating[co2Rating[:,i]=='0']
        #co2Rating = input[input[:,i]==1] if len(input[input[:,i]==1]) < len(input[input[:,i]==0]) else input[input[:,i]==0]
        #print(i)
        #print(co2Rating)
        #print('.............')
        if len(co2Rating) == 1: #只剩一行时，停止循环
            break
    oxygenRating = oxygenRating.tolist()    #将np.array数组转换为list
    oxygenRating = oxygenRating[0]          #由于转换后数据仍然是二维，需要先降维再转换为string
    #print(oxygenRating)
    oxygenRating = int(''.join(oxygenRating),2) #将元素组合为string，然后从二进制转换为十进制数据
    co2Rating = co2Rating.tolist()
    co2Rating = co2Rating[0]
    co2Rating = int(''.join(co2Rating),2)
    #print(oxygenRating)
    #print(co2Rating)
    return oxygenRating*co2Rating

#def webop(url):
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#    req = urllib.request(url=url, headers=headers)
#    x = urllib.request.urlopen(req).readlines()
#    print(len(x))


if __name__ == '__main__':
    print(powerConsumption('..\\files\\Day 3 data.txt'))
    #webop("https://adventofcode.com/2021/day/3/input")
    #webop('https://www.google.com')
    print(lifeSupportRating('..//files//Day 3 data.txt'))