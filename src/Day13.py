"""
# -*- coding: utf-8 -*-
@Created on 2:04 2022-01-23

@Describe:
https://adventofcode.com/2021/day/13

@author: TK
"""
import time
import matplotlib.pyplot as plt

def foldPaper(file, cmdNum):
    with open(file, 'r') as f:
        inputData = f.readlines()
    inputData = ''.join(inputData).split('\n')
    dotsList = []
    foldCmdList = []
    for x in inputData:
        if ',' in x:
            a, b = x.split(',')
            dotsList.append([int(a),int(b)])
        elif 'fold' in x:
            axisName, position = x.split(' ')[-1].split('=')
            foldCmdList.append([axisName,int(position)])
    print(dotsList)
    print(len(dotsList))
    #print(foldCmdList)
    axisName, position = foldCmdList[cmdNum-1]
    result = []
    if axisName == 'x':
        for x in dotsList:
            if x[0] > position:
                result.append(str(x[0]-2*(x[0]-position))+'-'+str(x[1]))
            else:
                result.append(str(x[0])+'-'+str(x[1]))
    else:
        for x in dotsList:
            if x[1] > position:
                result.append(str(x[0])+'-'+str(x[1]-2*(x[1]-position)))
            else:
                result.append(str(x[0]) + '-' + str(x[1]))
    print(result)
    return len(set(result))

def readDigits(file):
    with open(file, 'r') as f:
        inputData = f.readlines()
    inputData = ''.join(inputData).split('\n')
    dotsList = []
    foldCmdList = []
    for x in inputData:
        if ',' in x:
            a, b = x.split(',')
            dotsList.append([int(a),int(b)])
        elif 'fold' in x:
            axisName, position = x.split(' ')[-1].split('=')
            foldCmdList.append([axisName,int(position)])
    #print(dotsList)
    #print(len(dotsList))
    #print(foldCmdList)
    result = dotsList.copy()
    for i in range(len(foldCmdList)):
        axisName, position = foldCmdList[i]
        for j in range(len(result)):
            if axisName == 'x':
                if result[j][0] > position:
                    result[j][0] = result[j][0]-2*(result[j][0]-position)
            else:
                if result[j][1] > position:
                    result[j][1] = result[j][1]-2*(result[j][1]-position)
    #print(result)
    x = [a[0] for a in result]
    y = [-a[1] for a in result] #????????????????????????????????????????????????y=0??????????????????????????????????????????
    print(min(y))
    plt.ylim((-15,15))          #??????y???????????????????????????
    plt.scatter(x,y)
    plt.show()      #??????Y?????????????????????????????????????????????????????????
    #return result


if __name__ == '__main__':
    time_start = time.perf_counter()  # ??????????????????????????????
    #print(foldPaper('..//files//Day 13 data.txt',1))
    print(readDigits('..//files//Day 13 data.txt'))
    time_end = time.perf_counter()  # ??????????????????????????????
    print(time_end - time_start)  # ???????????????????????????
