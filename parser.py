class Book:
    def __init__ (self, id, rating):
        self.id = id
        self.rating = rating

class Lib:
    def __init__(self, books, signup_days, books_per_day):
        self.total_books = len(books)
        self.signup_days = signup_days
        self.books_per_day = books_per_day
        self.books = books
        self.alive = True

TOTAL_BOOKS = 0
TOTAL_LIBS = 0
TOTAL_DAYS = 0
BOOK_SCORES = []
LIBRARIES = []

with open("a_example.txt", "r") as a:
    TOTAL_BOOKS, TOTAL_LIBS, TOTAL_DAYS = list(map(int, a.readline().split(" ")))
    BOOK_SCORES = list(map(int, a.readline().split(" ")))
    for _ in range(TOTAL_LIBS):
        total_books, signup_days, books_per_day = list(map(int, a.readline().split(" ")))
        book_ids = set(map(int, a.readline().split(" ")))
        books = [Book(id, BOOK_SCORES[id]) for id in book_ids]
        lib = Lib(books, signup_days, books_per_day)
        LIBRARIES.append(lib)


print(TOTAL_BOOKS, TOTAL_LIBS, TOTAL_DAYS)
print(BOOK_SCORES)
print(LIBRARIES)