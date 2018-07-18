from collections import Counter
from heapq import heappush, heappop

class Huffman:
    """ Huffman encoding data """
   
    def __init__(self):
        self.data = ""
        

    def frequency(self,texto):
        """ This get the number letters from file """        
        return Counter(texto)

    def joined_nodes(self,nodeA,nodeB):
        print(nodeA[0])
        print(nodeB[0])
        frequency = nodeA[0] + nodeB[0]
        print(frequency)
        join = (frequency, None, nodeA, nodeB)
        return join


    def prefixos(self,dataFrequency):
        print(dataFrequency)
        dataNodes = []
        for char, freq in dataFrequency.items():
            heappush(dataNodes, (freq, char))

        while len(dataNodes) > 1:
            nodeA = heappop(dataNodes);
            nodeB = heappop(dataNodes);
            join = self.joined_nodes(nodeA,nodeB)
            print(dataNodes)
            print(join)
            heappush(arvore, join)
#            heappush(arvore,join)

    def doTree(self,dict):
        pass


    def readFile(self,path):
        """ Read the file from data """

        with open(path) as f:
            read_data = f.read()
            self.data = read_data;
            f.closed
        
        data  = self.frequency(self.data)
        self.prefixos(data)


data = Huffman()
data.readFile('data/input_1.txt')
