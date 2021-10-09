class Node:
    def __init__(self, value, preNode= None):
        self.value = value
        self.preNode = preNode
    
        
    def traversalLeafToRoot(self):
        tempNode = self
        path = [tempNode.value]
        while(True):
            if tempNode.preNode is None:
                break
            else:
                tempNode = tempNode.preNode
                path.append(tempNode.value)
        
        path = path[::-1]
        return path

# use binary tree with array, and tracking path with NodeList
# a[i] is father of a[2i+1] and a[2i+2]
def findMinimumOperator(x, y):
    result = []
    binary_ar = [Node(value = x)]
    isMinus = True
    i = 0
    while(True):
        if isMinus:
            new_index = len(binary_ar)
            father_node = binary_ar[(new_index-1)//2]
            father_node_value =  binary_ar[(new_index-1)//2].value
            new_node = Node(value = (father_node_value-1), preNode = father_node)
            binary_ar.append(new_node)
            isMinus = not isMinus
            if new_node.value == y:
                return new_node.traversalLeafToRoot()
        else:
            new_index = len(binary_ar)
            father_node = binary_ar[(new_index-2)//2]
            father_node_value =  binary_ar[(new_index-2)//2].value
            new_node = Node(value = (father_node_value*2), preNode = father_node)
            binary_ar.append(new_node)
            isMinus = not isMinus
            if new_node.value == y:
                return new_node.traversalLeafToRoot()

def prinResultPretty(path, result):
    for i in range(len(path)-1):  
        if (path[i]-1) == path[i+1]:
            print(f'{path[i]} - 1 = {path[i]-1}')
        if (path[i]*2) == path[i+1]:
            print(f'{path[i]} * 2 = {path[i]*2}')

if __name__  == '__main__':
    x = 3
    y = 100
    p = findMinimumOperator(x, y)
    prinResultPretty(p, y) 