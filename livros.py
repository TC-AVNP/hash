

class Book:
    def __init__ (self, id, rating):
        self.id = id
        self.rating = rating


class Lib:
    def __init__(self, books, warmup, books_per_day, id):
        self.id = id
        self.total_books = len(books)
        self.warmup = warmup
        self.books_per_day = books_per_day
        self.bookIndex = 0
        self.books = sorted(books, key=lambda x: x.rating, reverse=True)
        self.day = -1
        self.value = totalValue(books, books_per_day, warmup)
        
        
    def shipBooks(self):
        totalScanningDays = TOTAL_DAYS - self.day - self.warmup
        totalBooks = min(totalScanningDays * self.books_per_day, len(self.books)) 
        return self.books[0:totalBooks-1]



def totalValue(books, books_per_day,warmup):
    value = 0
    for b in books:
        value += b.rating
    return  value/(len(books)/books_per_day + warmup)


def bestLib(libs, day):
    best = 0
    lib = Lib(1,1,1,-1)
    for l in libs:
        if best < lib.value:
            best = lib.value
            lib = l
    lib.day = day    
    return lib








TOTAL_BOOKS = 0
TOTAL_LIBS = 0
TOTAL_DAYS = 0
BOOK_SCORES = []
LIBRARIES = []
BOOK_IDS_PER_LIB = []
LIBS_TO_SIGNUP = []
TOTAL_BOOKS_PER_LIB = []



def writeln(out, text):
    out.write(str(text))
    out.write("\n")

def write_output(lib_ids, total_books_per_lib, book_ids_per_lib):
    with open("output.txt", "w") as out:
        writeln(out, len(lib_ids))
        writeln(out, " ".join(map(str, lib_ids)))
        for i in range(len(lib_ids)):
            writeln(out, str(lib_ids[i]) + " " + str(total_books_per_lib[i]))
            writeln(out, " ".join(map(str, book_ids_per_lib[i])))




    
if __name__ == "__main__":
    with open("a_example.txt", "r") as a:
        TOTAL_BOOKS, TOTAL_LIBS, TOTAL_DAYS = list(map(int, a.readline().split(" ")))
        BOOK_SCORES = list(map(int, a.readline().split(" ")))
        for id in range(TOTAL_LIBS):
            total_books, warmup, books_per_day = list(map(int, a.readline().split(" ")))
            book_ids = set(map(int, a.readline().split(" ")))
            books = [Book(id, BOOK_SCORES[id]) for id in book_ids]
            lib = Lib(books, warmup, books_per_day, id)
            LIBRARIES.append(lib)

    books_per_lib = []
    DAY = 0
    while DAY < TOTAL_DAYS :
        bestLib = bestLib(LIBRARIES, DAY)
        books = bestLib.shipBooks()
        BOOK_IDS_PER_LIB.append(books) 
        TOTAL_BOOKS_PER_LIB.append(len(books))
        LIBS_TO_SIGNUP.append(bestLib.id)
        DAY += bestLib.warmup
        
        
    write_output(LIBS_TO_SIGNUP, TOTAL_BOOKS_PER_LIB, BOOK_IDS_PER_LIB)
