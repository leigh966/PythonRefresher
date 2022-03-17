def basicExample():
    class ClassTest:
        def instance_method(self): # Action of object
            print(f"Called instance_method of {self}")
        
        @classmethod
        def class_method(cls): # Used as factories
            print(f"Called class_method of {cls}")
        
        @staticmethod
        def static_method(): # Just a function owned by a class
            print("Called static_method")

    ClassTest.static_method()
    ClassTest.class_method()
    ClassTest().instance_method()
basicExample()

def factoryExample():
    class Book:
        TYPES = ("hardcover", "paperback")

        def __init__(self, name, book_type, weight):
            self.name = name
            self.book_type = book_type
            self.weight = weight

        def __repr__(self):
            return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

        @classmethod
        def hardcover(cls, name, page_weight):
            return cls(name, cls.TYPES[0], page_weight+100)

        @classmethod
        def paperback(cls, name, page_weight):
            return cls(name, cls.TYPES[1], page_weight)

    book1 = Book.hardcover("Harry Potter", 276)
    book2 = Book.paperback("Python 101", 308)
    print(book1)
    print(book2)

factoryExample()