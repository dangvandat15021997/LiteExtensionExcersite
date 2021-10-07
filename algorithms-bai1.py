# Find continue subset of an array
# Example input: ['1','2','3'] 
# output: [
#          ['1'],
#          ['2'],
#          ['3'],
#          ['1','2'],
#          ['2','3']
#                    ]
def findContinueSubSet(ar):
    if len(ar) == 1:
        return [[ar[0]]]
    else:
        base = findContinueSubSet(ar[:-1])
        operator = ar[-1:]
        next_base = base
        next_base.append(operator)
        for i in base:
            if int(i[-1]) == (int(operator[0]) - 1):
                new_item = i + operator
                next_base.append(new_item)  
        return next_base
                            

# Find all subset which do not have common value
# Example 
# input: [
#         ['1','2'],
#         ['2','3'],
#         ['5','6']
#                  ]
# output: [
#          [['1','2'], ['5','6']],
#          [['2','3'],['5','6']]
#                               ]

def powerSetCheckCommon(inputList):
    # example
    # input ar1 = [1,2] ar2 = [3,4] output: False
    # input ar1 = [1,2] ar2 = [1,4] output: True
    # input ar1 = [1,2] ar2 = [[5,6],[2,3]] output: True
    def checkCommonValue(ar1, ar2):
        check = False
        for item1 in ar1:
            for item2 in ar2:
                if set(item1) & set(item2):
                    check = True
                    break
        return check  
    if len(inputList) == 0:
        return [[]]
    else:
        base = powerSetCheckCommon(inputList[:-1])
        operator = inputList[-1:]
        next_base = base[:]
        for b in base:
            try:
                if not checkCommonValue(b, operator):                
                    newItem = b + operator
                    next_base.append(b + operator)
            except:
                print(f'in catch: B {b}, operator: {operator}')
        return next_base

        # Example:
# input numbers = ['1','2'], tail = 6 output: [['1','2'], '3', '4', 5]
# input numbers = ['5','6'], head = 10, tail = 1  output: ['1','2', '3', '4', ['5','6'],'7','8','9']
def fillNumber(numbers, **kwargs):
    result = []
    headList = []
    tailList = []
    if 'head' in kwargs.keys():
        headList = [str(x) for x in range(kwargs['head'],int(numbers[0]))]
    if 'tail' in kwargs.keys():
        tailList = [str(x) for x in range(int(numbers[-1])+1, kwargs['tail'])]
    new_numbers = ["".join(numbers)]
    
    result = headList + new_numbers + tailList
    return result

    #Convert string to numbersLisy
# Example
# input [['3','4'], ['7','8']] output = [1,2,34,5,6,78,9]
# input [['1','2']] output = [12,3,4,5,6,7,8,9]
def convertToNumbers(stringNumberList):
    # Example:
    # input numbers = ['1','2'], tail = 6 output: [['1','2'], '3', '4', 5]
    # input numbers = ['5','6'], head = 10, tail = 1  output: ['1','2', '3', '4', ['5','6'],'7','8','9']  
    def fillNumber(numbers, **kwargs):
        result = []
        headList = []
        tailList = []
        if 'head' in kwargs.keys():
            headList = [str(x) for x in range(kwargs['head'],int(numbers[0]))]
        if 'tail' in kwargs.keys():
            tailList = [str(x) for x in range(int(numbers[-1])+1, kwargs['tail'])]
        new_numbers = ["".join(numbers)]
        result = headList + new_numbers + tailList
        return result
    
    
    new_list = []
    result = []
    if len(stringNumberList) == 1:
        result = fillNumber(stringNumberList[0], head=1, tail=10)
    elif len(stringNumberList) == 2:
        result =  fillNumber(stringNumberList[0],head = 1)+ fillNumber(stringNumberList[1],head = int(stringNumberList[0][-1])+1, tail = 10)
    else:
        new_list = []
        for i in range(len(stringNumberList)):
            if(i == 0):
                new_list.append(fillNumber(stringNumberList[i],head = 1))
            elif(i == len(stringNumberList) - 1):
                new_list.append(fillNumber(stringNumberList[i],tail = 10))
            else:
                new_list.append(fillNumber(stringNumberList[i], head = int(stringNumberList[i-1][-1])+1, tail = int(stringNumberList[i+1][0])))
        result =  new_list
        
    try:
        result = sum(result, [])
        return [int(x) for x in result]
    except:
        return [int(x) for x in result]

# Print result with signs
# Example input:  [12,3,4,5], target = 6 minusPosition = [2,3]
# ouput '12+3-4-5 = 6'
def toStringResult(numberList, minusPosition, target):
    s = str(numberList[0])
    for i in range(1, len(numberList)):
        if i in minusPosition:
            s = s + ' - ' + str(numberList[i])
        else:
            s = s + ' + ' + str(numberList[i])
        
        if (i == (len(numberList)-1)): 
            s = s + ' = ' + str(target)
    return s

#Find all subset have sum = target
# Example input: numbers = [1,2,4,5,6] target = 6 ouput [[6], [1,5], [2,4]]
def findSubsetSum(numbers, target, partialIndex=[], remainIndex = 0, resultList = []):
    resultList = resultList
    if not partialIndex:
        partial = []
    else:
        partial = [numbers[x] for x in partialIndex]
    s = sum(partial)
    
    # check if the partial sum is equals to target
    if s == target: 
        resultList.append(partialIndex)
    if s >= target:
        return  # if we reach the number return
    
    for i in range(remainIndex, len(numbers)):
        newIndex = i
        remainIndex += 1
        findSubsetSum(numbers, target, partialIndex + [newIndex], remainIndex, resultList) 
        
    return resultList

def findSign(numbers, target):
    # Find subset contain continueosly elements like ['1','2'] or ['7','8','9']
    subSetContinue = findContinueSubSet(test)
    # Drop single element subset like ['1'], ['2'] 
    newSubSetContinue = []
    for i in range(len(subSetContinue)):
        if (len(subSetContinue[i]) > 1):
            newSubSetContinue.append(subSetContinue[i])
            
    # Find all possible sequen with None 
    sequenceWithNone = powerSetCheckCommon(newSubSetContinue)
    sequenceWithNone = sequenceWithNone[1:]
    
    for sequence in sequenceWithNone:
        sequence = convertToNumbers(sequence)
        # default sequen with start with all + 
        # For example [123,4,5,6,7,8,9] start with 123+4+5+6+7+8+9
        # each time replace + with - we minus -2x(number before the sign)
        # for example (123+4+5+6+7+8+9) - (123+4+5+6+7-9) = 2x9 
        # So we need to find all position of Minus sign so that have sum = |100 - sum(sequence)| 
        # Example [123,4,5,6,7,8,9] find position of Minus so sum = |100 - (123+4+5+6+7+8+9)| = 62
        # Result is 123 - 4 - 5 - 6 - 7 + 8 - 9 = 100
        # if sum == 100 print result
        if sum(sequence) == 100:
            print(toStringResult(sequence, [x for x in range(1, len(sequence))]))
        # if sum < 100 so all signal is + so we need to change sequence
        elif sum(sequence) < 100:
            continue
        # 
        else:
            targetSum = abs(100 - sum(sequence))
            minusPositionList = findSubsetSum([x*2 for x in sequence], targetSum, resultList = [])     
            if minusPositionList:
                for minusPosition in minusPositionList:
                    print(toStringResult(sequence, minusPosition, target = 100))  

if __name__ == '__main__':
    test = ['1','2','3','4','5','6','7','8','9']
    findSign(test,100)

    
    
