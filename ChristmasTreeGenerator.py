
class ChristmasTreeGenerator:

    def __init__(self, height, tallOrShort):
        self.height = height
        self.tallOrShort = tallOrShort
        ChristmasTreeGenerator.bottomUpTree(height, tallOrShort)

    def bottomUpTree(height, tallOrShort):
        treeArray = [""] * height
        for treeRow in range(height, 0, -1):
            spaces = height - treeRow
            stringSpaces = ""
            for eachSpace in range (spaces):
                stringSpaces += " "

            treeString = stringSpaces
            for rowLength in range(treeRow):
                treeString += "* "
            index = treeRow - 1
            treeArray.insert(index, treeString)
        
        for index in range(len(treeArray)):
            print(treeArray[index])
        
        
        for oddIndex in range(1, len(treeArray), 1):
            del treeArray[oddIndex: oddIndex + 1] 

        for index in range(len(treeArray)):
            print(treeArray[index])
