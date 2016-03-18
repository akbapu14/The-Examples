"""
>>>minglish(["y", "z", "xy"])
"yzx"

>>>minglish(["ba", "ab", "cb"])
"bac"

>>>minglish(["ba", "bb", "bc"])
"abc"
>>>minglish(["baasdfdasdfd", "baasdfdasdfe", "baasdfdasdff", "baasdfdasdfg"])
"defg"
"""
# function that first goes through the first element, adds what we know so far to an ordered list
# goes through the n element of words which have the same letter before
# [ xzy, xzf]
class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)


def minglish(someList):
    finalOrder = []
    def minglishHelper(someList):
        orderedNewList = []
        for i in range(len(someList)):
            try:
                if someList[i][0] not in orderedNewList:
                    orderedNewList.append(someList[i][0])
            except IndexError:
                pass
        finalOrder.append(orderedNewList)
        for i in samePrevOrderer(someList):
            minglishHelper(i)
    minglishHelper(someList)
    finalOrder = popOffOneLetterWords(finalOrder)
    return mergeLists(finalOrder)

def popOffOneLetterWords(someshortedList):
    for i in range(len(someshortedList)):
        if len(someshortedList[i]) <= 1:
            someshortedList.pop(i)
            return popOffOneLetterWords(someshortedList)
        else:
            pass
    return someshortedList

#takes off first letter and groups
def samePrevOrderer(someList):
    #list of lists
    newordereredlist = []
    def samePrevOrdererHelper(someshortedList):
        if someshortedList:
            someshortedList = popOffOneLetterWords(someshortedList)
            if someshortedList:
                groupedlist = []
                letter = someshortedList[0][0]
                for i in range(len(someshortedList)):
                    if someshortedList[i][0] == letter:
                        groupedlist.append(someshortedList[i][1:])
                        if i == len(someshortedList) - 1:
                            newordereredlist.append(groupedlist)
                    else:
                        newordereredlist.append(groupedlist)
                        samePrevOrdererHelper(someshortedList[i:])
    samePrevOrdererHelper(someList)
    return newordereredlist

def mergeLists(finalOrder):
    orderDict = {}
    def mergeListsRecurse(finalOrder):
        if finalOrder:
            for i in range(len(finalOrder[0]) -1):
                orderDict[finalOrder[0][i]] = finalOrder[0][i + 1]
            if len(finalOrder) > 1:
                mergeListsRecurse(finalOrder[1:])
    mergeListsRecurse(finalOrder)
    finalOrder = []
    prev = None
    done = False
    for key in orderDict:
        if key not in orderDict.values():
            finalOrder.extend([key, orderDict[key]])
            prev = orderDict[key]
    while not done:
        if len(finalOrder) == len(list(orderDict.values())) + 1:
            done = True
        else:
            finalOrder.extend(orderDict[prev])
            prev = orderDict[prev]
    return ''.join(finalOrder)
