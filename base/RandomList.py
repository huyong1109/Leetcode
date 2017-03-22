### Lists of random integers
### e.g [ [1, 2], [1,1,1], ...]
import random

class RandomList(object):
    def __init__(self, items):
        self.items = items
        print('List memebers: ')
        print(items)
     
    def createRandomList(self, listSize=1, length=100, randomsize=True, sort=False):
        """
        :type listsize: int 
            number of strings will be created
        :type length: int
            length of string
        :type randomsize: bool
            True: random length for each string
            False: same length for all strings
        :rtype: [String]
            list of strings
        """
        random.seed(1314)
        re = []

        try:
            if randomsize:
                lengths = [random.choice(range(1, length + 1)) for i in range(listSize)]
            else:
                lengths = [length]*listSize
        except Exception as e:
            print(e)
            print('Check parameters in createRandomList')

        if sort:
            re = [sorted([random.choice(self.items) for i in range(length)]) for length in lengths]
        else:
            re = [[random.choice(self.items) for i in range(length)] for length in lengths]

        return re

    def createNonDuplicateList(self, listSize=1, length=100, randomsize=True, sort=False):
        """
        :type listsize: int 
            number of strings will be created
        :type length: int
            length of string
        :type randomsize: bool
            True: random length for each string
            False: same length for all strings
        :rtype: [String]
            list of strings
        """
        random.seed(1314)
        re = []
        if length > len(self.items):
            print('length larger than the size of items, set to {} already!'.format(len(self.items)))
            length = len(self.items)
        try:
            if randomsize:
                lengths = [random.choice(range(1, length + 1)) for i in range(listSize)]
            else:
                lengths = [length]*listSize
        except Exception as e:
            print(e)
            print('Check parameters in createRandomList')

        if sort:
            re = [sorted(random.sample(self.items, length)) for length in lengths]
        else:
            re = [random.sample(self.items, length) for length in lengths]

        return re



class StringList(RandomList):
    # character sets
    # all ASCII characters
    AsciiChar = [chr(i) for i in range(256)] 

    # all ASCII characters
    LowerAlphaBeta = AsciiChar[97:122]
    UpperAlphaBeta = AsciiChar[65:90]
    AlphaBeta = LowerAlphaBeta + UpperAlphaBeta

    Chars = [AsciiChar, AlphaBeta, LowerAlphaBeta, UpperAlphaBeta]

    def __init__(self, charSetInd=0):
        """
        :type charSetInd : int  choose the character type
            0: all characters in ASCII table
            1: full alphabeta 
            2: lower case alphabetas
            3: upper case alphabetas
        """
        charSet = self.Chars[charSetInd]
        RandomList.__init__(self, charSet)


    
    def createRandomString(self, size=1, length=100, randomsize=True):
        """
        :type size: int 
            number of strings will be created
        :type length: int
            length of string
        :type randomsize: bool
            True: random length for each string
            False: same length for all strings
        :rtype: [String]
            list of strings
        """
        re = [''.join(L) for L in RandomList.createRandomList(self, size, length)]


        return re


class IntList(RandomList):

    def __init__(self, IntMin, IntMax):
        """
        :type Range : int  
            choose int from range(min, max)
        """
        
        RandomList.__init__(self, range(IntMin, IntMax+1))

    

