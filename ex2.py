from book import Book

# Создаем список книг (библиотеку)
library = [
    Book("Гарри Поттер и орден Феникса", "Джоан Роулинг"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]

# Печатаем библиотеку
for book in library:
    print(f"{book.title} - {book.author}")