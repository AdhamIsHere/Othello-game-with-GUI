class Cell:
    def __init__(self,color):
        self.__color = color

    def flip(self):
        if self.__color == 'black':
            self.__color = 'white'
        else:
            self.__color = 'black'

    def setColor(self,color):
        self.__color = color.lower()

    def getColor(self):
        return self.__color

    def isEmpty(self):
        return self.__color == ''
