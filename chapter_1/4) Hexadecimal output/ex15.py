def name_triangle():
    name = input("Enter your name: ")
    
    for i, char in enumerate(name, 1):
        print(name[:i])

name_triangle()