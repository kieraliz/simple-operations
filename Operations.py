class Operations:

    def treeSpaces(self, height, treeRow):
        spaces = height - treeRow
        stringSpaces = ""
        for oneSpace in range (spaces):
            stringSpaces += " "
        treeString = stringSpaces

    def ChristmasTree(height):
        treeArray = [""] * height
        for treeRow in range(height, 0, -1):
            spaces = height - treeRow
            stringSpaces = ""
            for oneSpace in range (spaces):
                stringSpaces += " "
            treeString = stringSpaces

            for rowLength in range(treeRow):
                treeString += "* "
            index = treeRow - 1
            treeArray.insert(index, treeString)
        
        for oddIndex in range(1, len(treeArray), 1):
            del treeArray[oddIndex: oddIndex + 1] 

        for index in range(len(treeArray)):
            print(treeArray[index])
    
    
