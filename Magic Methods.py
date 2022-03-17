def Str():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return f"{self.name}: {self.age}"

    p1 = Person("Bob", 18)
    print(p1)
Str()

def repr():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f"<Person - name={self.name}, age={self.age}>"
    p1 = Person("Bob", 18)
    print(p1)
repr()

