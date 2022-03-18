class TooManyPagesReadError(ValueError):
    def __init__(self, max : int, current : int):
        super().__init__(
            f"You tried to read {current} pages but there are only {max}"
        )

class Book:
    def __init__(self, total_pages : int):
        self.total_pages=total_pages
        self.pages_read = 0
    def read(self, pages : int):
        new_read_count = self.pages_read + pages
        if new_read_count > self.total_pages:
            raise TooManyPagesReadError(self.total_pages, new_read_count)
        self.pages_read = new_read_count
        print(f"{self.pages_read} pages read out of {self.total_pages}")

book = Book(50)
for num in range(2):
    try:
        book.read(30)
    except TooManyPagesReadError as e:
        print(e)