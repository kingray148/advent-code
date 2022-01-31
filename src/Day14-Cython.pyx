def polymer(file, step):
    cdef std::string inputdata
    with open(file, 'r') as f:
        inputData = f.readlines()
    inputData = ''.join(inputData).split('\n')
    polymerDict = {}
    for x in inputData:
        if x != '' and '->' not in x:
            initialState = x.strip()
        elif '->' in x:
            pair, element = x.split('->')
            pair = pair.strip()
            element = element.strip()
            polymerDict[pair] = element
    #print(polymerDict)
    #print(repr(initialState))
    result = initialState
    for i in range(0, step):
        temp = ''
        for j in range(len(result)-1):
            temp += result[j] + polymerDict[result[j:j+2]]
        temp += result[-1]
        result = temp
        print(i)
    resultDict = {}
    for x in list(result):
        resultDict[x] = resultDict.get(x,0) + 1
    print(resultDict)
    return (max(resultDict.values()) - min(resultDict.values()))