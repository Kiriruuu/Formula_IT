# TODO Найдите количество книг, которое можно разместить на дискете
storage = (1.44 * 1024 ** 2)
one_symbol = 4
one_string = one_symbol * 25
one_paper = one_string * 50
one_book = one_paper * 100
total_books = storage / one_book
total_books = int(total_books)
print("Количество книг, помещающихся на дискету:",total_books)