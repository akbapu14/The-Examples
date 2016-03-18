print("hello")
def sorted(list1):
    if not list1:
        return []
    if len(list1) == 1:
        return list1
    for i in range(0, len(list1) - 1):
        if not (list1[i] <= list1[i + 1]):
            exit
        if i == len(list1) -1:
            return list1
    middle = list1[len(list1) // 2]
    left = []
    right = []
    middlelist = []
    for i in range(0, len(list1)):
        if list1[i] < middle:
            left.append(list1[i])
        elif list1[i] > middle:
            right.append(list1[i])
        else:
            middlelist.append(list1[i])
    return sorted(left) + middlelist + sorted(right)


def sum_N(A, N):
    d = {}
    l = []
    for i in A:
        if (N-i) not in d:
            d[i] = 1
        else:
            l.append((i, N-i))

    return d

def make_change(value, coinList):
    if value == 0:
        return 1
    elif value < 0:
        return 0
    elif not coinList:
        return 0
    else:
        withLargestCoin = make_change(value - coinList[0], coinList[1:])
        withoutLargestCoin = make_change(value, coinList[1:])
        return (withoutLargestCoin + withLargestCoin)
def make_changeconstant(value, coinList):
    listkeeper = []
    coinList.sort()
    def helper(value, coinList):
        if value == 0:
            listkeeper.append(1)
            return
        elif value < 0:
            return
        elif not coinList:
            return
        else:
            for i in coinList:
                if i > value:
                    helper(value, coinList[1:])
                else:
                    listkeeper.append(i)
                    helper(value - i, coinList)
    helper(value, coinList)
    if listkeeper:
        return sum(listkeeper)

    else:
        return 0
class DirectedGraph:
    def __init__(self,content):
        self.content = content
        self.neighbours = []

n1 = DirectedGraph(1)
n2 = DirectedGraph(2)
n3 = DirectedGraph(3)
n4 = DirectedGraph(4)
n5 = DirectedGraph(5)

n1.neighbours.append(n2)
n2.neighbours.append(n3)
n2.neighbours.append(n4)
n4.neighbours.append(n5)
n4.neighbours.append(n1)

graph1 = {n1: [n2, n3],
n2: [n1, n3],
n3: [n1,n2]}

def pathexdepth(start, end, alreadyvisited = []):
    if start == end:
        return True
    elif not start or not end:
        return False
    elif end in start.neighbours:
        return True
    elif start in alreadyvisited:
        return alreadyvisited
    else:
        alreadyvisited += [start]
        for neighbour in start.neighbours:
            return pathexdepth(neighbour, end, alreadyvisited)


def is_route_between2(node1, node2):
    if node1 is node2:
        return True
    elif node1 is None or node2 is None:
        return False
    visited = set([node1, node2])
    from Queue import deque
    queue = deque([node1])
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.neighbours:
            if child is node2:
                return True
            elif child not in visited:
                visited.add(child)
                queue.append(child)
                print(queue)
    return False


def oddManOut(list1):
    intVal = 0
    for i in list1:
        (a and not b) or (not a and b)

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)
    return visited

#
#
#   |
# |   |
# ||  ||
def dfstree(headNode, searchValue):
    stack = []
    visited = {}
    stack.append(headNode)

    while stack:
        if currentNode == searchValue:
            return True
        currentNode = stack.pop()
        for node in currentNode.childen:
            if node not in visited:
                stack.append(node)

    return False

def mergeSort(list1):
    if len(list1) <= 1:
        return list1
    length1 = len(list1)
    left = mergeSort(list1[:length1//2])
    right = mergeSort(list1[length1//2:])
    return merge(left, right)
#
# [1,2,2,3,4] [2, 3, 5]
#
# [1,2,2,3,4,5]

def merge(left, right):
    newList = []
    leftLength = len(left) - 1
    rightLength = len(right) - 1
    i = 0
    j = 0

    while i <= leftLength and j <= rightLength:
        if left[i] < right[j]:
            newList.append(left[i])
            i += 1
        elif right[j] < left[i]:
            newList.append(right[j])
            j += 1
        else:
            newList.append(left[i])
            i += 1
            j += 1
    if leftLength > rightLength:
        for i in left[i:]:
            newList.append(i)
    else:
        for i in right[j:]:
            newList.append(i)
    return newList

    class Tree:
        def __init__(self, node, left = None, right = None):
            self.node = node
            self.left = left
            self.right = right

    def allpaths(node):
        stack = []
