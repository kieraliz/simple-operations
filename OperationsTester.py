from Operations import Operations

class createOperations():
    def christmasTree(self):
        while True:
            height = (int(input("Enter the tree height: ")))            
            if (height < 2): print("Invalid Height: Height is too small")
            if (height >= 63): print("Invalid Height: Height is too large")
            if (2 <= height & height <= 62): break
        print()
        Operations.ChristmasTree(height)

class Menu:
    while True:
        print()
        print("Select an Operation")
        print("[1] Christmas Tree")
        print("[Q] Quit")

        response = (input(">> ").lstrip().rstrip())

        if (response == "Q"): break
        if (response == '1'): createOperations().christmasTree()

        else:
            print()
            print("Type a valid Operation")

menu = Menu()