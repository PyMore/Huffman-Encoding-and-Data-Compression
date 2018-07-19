from collections import Counter
from heapq import heappush, heappop,heapify

class Huffman:
    """ Huffman encoding data """
   
    def __init__(self):
        self.data = ""
        

    def frequency(self,texto):
        """ This get the number letters from file """        
        return Counter(texto)

    def joined_nodes(self,nodeA,nodeB):
        frequency = nodeA[1] + nodeB[1]
        join = (frequency, nodeA, nodeB)
        return join


    def prefixos(self,dataFrequency):

        frequArray= list(Counter(dataFrequency).items())
        heapify(frequArray)
        data = []

        while len(frequArray) > 1:
            nodeA = heappop(frequArray);
            nodeB = heappop(frequArray);
            join = self.joined_nodes(nodeA,nodeB)   
            heappush(data, join)
        print(data)




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
