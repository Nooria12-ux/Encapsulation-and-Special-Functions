class IOString:
    
    def __init__(self):
        self.__word = ""
        
    def inputString(self):
        self.__word = input("Enter your precious name: ")
        
    def revString(self):
        return self.__word[::-1]
    
word = IOString()

word.inputString()

print(f"Your Reversed name: {word.revString()}")            