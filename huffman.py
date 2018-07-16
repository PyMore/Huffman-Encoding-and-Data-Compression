from heapq import heappush, heappop
import numpy as np

class Huffman:
    """ Huffman encoding data """
   
    def __init__(self):
        self.data = ""
        self.dataNumber = []


    def showData(self,data):
        print(data)


    def readFile(self,path):
        """ Read the file from data """
        with open(path) as f:
            read_data = f.read()
            self.data = read_data;
            f.closed


    def getNumberLetters(self):
        """ This get the number letters from file """

        letters = [ letter for letter in self.data] 
        letters = set(letters)

        for letter in letters:
            dic = {}
            count = self.data.count(letter)
            dic['letter'] = letter
            dic['count'] = count
            self.dataNumber.append(dic)

        sort = sorted(self.dataNumber,key= lambda x:x['count']\
            ,reverse=True)
        self.dataNumber = sort

        print(np.array(sort))


    def getBinary(self):
        
        word = {}
        for data in self.dataNumber:
            word = data
            word['binary'] = bin(word['count'])
            

        print(self.dataNumber)

    def getData(self):
        for letter in self.data:
            print(letter)

        return self.data.islower


data = Huffman()
data.readFile('data/input_1.txt')
data.getNumberLetters()
data.getBinary()