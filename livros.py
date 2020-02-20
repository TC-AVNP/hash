

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
        self.choosen = False
        self.scanning = False



    def totalValue(self):
        value = 0
        for b in self.books:
            value += BOOK_SCORES[b]

        self.Valeu =  value/(len(self.book_ids)/self.books_per_day + self.signup_days)

    def tick(self):


        return        




    



def chooseLib(): 
    best = 0 
    escolhida  = Lib(1,1,1)
    for l in LIBRARIES:
        if not l.Valeu: 
            continue
        if l.totalValue() > best:
            best = l.Valeu
            escolhida = l



    escolhida.alive = False
    return best





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
        lib = Lib(total_books, signup_days, books_per_day)
        lib.book_ids = set(map(int, a.readline().split(" ")))
        LIBRARIES.append(lib)
print(TOTAL_BOOKS, TOTAL_LIBS, TOTAL_DAYS)
print(BOOK_SCORES)
print(LIBRARIES)
