from RandomList import RandomList

### Matrix List of fixed-lenght lists 
### e.g [ [1, 2], [1,1], ...]

class Matrix(object):

    mat = []
    def __init__(self, matrix=None):
        if matrix:
            self.mat = matrix

    def setMat(self, matrix):
        self.mat = matrix
     
    def createRandomMat(self, m, n, items):
        """
        :type m: int 
            number of lists
        :type n: int
            length 
        """
        randomList = RandomList(items)
        self.mat = randomList.createRandomList(m, n, randomsize=False, sort=False) 
        return self.mat
        
    def getMat(self):
        return self.mat

    def printMat(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.mat]))


