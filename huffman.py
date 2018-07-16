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
        
        count =0
        temp = {}
        for letter in letters:
            for text in self.data:
                if letter is text:
                    count = count +1

            temp[letter] = count            
            self.dataNumber.append(temp)
            count= 0
        
        print(self.dataNumber)


    def orderLetters(self):
        """ This order the letters from data """
        pass

    def getData(self):
        for letter in self.data:
            print(letter)

        return self.data.islower


data = Huffman()
data.readFile('data/input_1.txt')
data.getNumberLetters()
