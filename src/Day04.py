"""
# -*- coding: utf-8 -*-
@Created on 3:36 2022-01-02

@Describe:
https://adventofcode.com/2021/day/4

@author: TK
"""

import numpy as np

def calculateScore(files):
    with open(files, 'r') as f:
        nums = f.readline()                                 #读取第一行数字
        content = f.readlines()                             #读取5x5数组原始数据
        while '\n' in content:                              #去除空行
            content.remove('\n')
    nums = nums.split(',')
    nums = [int(x) for x in nums]                           #将第一行数字转化为整数list
    #print(content)
    content = ''.join(content).split()                      #将读取数据转换为单行然后转换为字符串list
    content = [int(x) for x in content]                     #字符串list转为整数list
    blocknum = int(len(content)/25)                         #计算转换为三维数组的第一维数字
    content = np.reshape(content, (blocknum,5,5))           #将数据转换为多组的5x5数组（三维数组）
    #print(blocknum)
    #print(content)
    #below is to calculate score based on reading data
    #content[content == 60] = 0
    #print(content[85])
    for x in nums:                                          #对第一行数字进行遍历，找出使任一5x5数组出现行或列全部被标识的数字
        content[content == x] = -1                          #将标识出的数字替换为-1以便于计算（因数组中含有0，因此用-1替换以便计算
        if -5 in np.sum(content, axis=1):                   #如果数组中出现某一行全为-1，即全行数字被标识出来，则返回计算结果
        #    print('x='+str(x))
            for y in np.where(np.sum(content,axis=1)==-5):  #找出第一个符合行全为-1的数组（有可能多个数组同时出现某行为零情况）
        #        print('y='+str(y))
                content[y[0]][content[y[0]] == -1] = 0      #将该数组中所有之前标识为-1的整数重置为零，以便于计算剩余数字总和
                return sum(sum(content[y[0]]))*x
        elif -5 in np.sum(content, axis=2):                 #如果数组中出现某一列全为-1，即全行数字被标识出来，则返回计算结果
        #    print('x=' + str(x))
            for y in np.where(np.sum(content,axis=2)==-5):  #找出第一个符合列全为-1的数组（有可能多个数组同时出现某列为零情况）
        #        print('y='+str(y))
        #        print(content[y])
                content[y[0]][content[y[0]]==-1] = 0
        #        print(content[y])
                return sum(sum(content[y[0]]))*x


if __name__ == '__main__':
    print(calculateScore('..\\files\\Day 4 data.txt'))
