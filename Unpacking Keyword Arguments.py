def argsToDictionary():
    def named(**kwargs):
        print(kwargs)
    named(name="bob", age=20)
argsToDictionary()