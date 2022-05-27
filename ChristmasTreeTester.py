from ChristmasTreeGenerator import ChristmasTreeGenerator

height = int(input("Enter the tree height: "))
char = ((input("Tall or Short (T/S): ").lstrip()).rstrip())

if (char == "Tall"):
    ChristmasTreeGenerator(height, True)
