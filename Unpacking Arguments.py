def basicExample():
    def multiply(*args): # Args will be a tuple that can vary in length
        print(args)
        total = 1
        for arg in args:
            total *= arg
        return total
    print(multiply(-1))
    print(multiply(1))
    print(multiply(2,3))
    print(multiply(5,9,7))
basicExample()

def passingEachElementOfAList():
    def multiply(*args): # Args will be a tuple that can vary in length
        print(args)
        total = 1
        for arg in args:
            total *= arg
        return total
    nums = [2,5,7,9,12]
    print(multiply(*nums))
passingEachElementOfAList()

def dictionaryOfArguments():
    def add(x,y):
        return x+y
    nums = {"x":15, "y":5}
    print(add(**nums))
dictionaryOfArguments()