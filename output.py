TOTAL_LIBS_SIGNUP = 10
LIBS_TO_SIGNUP = [2,5,7]
TOTAL_BOOKS_PER_LIB = [2,5,7]
BOOK_IDS_PER_LIB = [
    [2,7],
    [4,7,8,9,1],
    [1,2,3,4,5,6,7]
]

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

write_output(LIBS_TO_SIGNUP, TOTAL_BOOKS_PER_LIB, BOOK_IDS_PER_LIB)