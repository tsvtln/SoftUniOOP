from project.user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books: {str: {str: int}} = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if self.__is_rented(book_name):
            return f"The book \"{book_name}\" is already rented and will be available in {self.rented_books[user.username][book_name]} days!"
        if not self.__book_in_library(book_name, author):
            return
        user.books.append(book_name)
        self.rented_books.setdefault(user.username, {})
        self.rented_books[user.username][book_name] = days_to_return
        self.books_available[author].remove(book_name)
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if not book_name in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        del self.rented_books[user.username][book_name]
        self.books_available[author].append(book_name)

    def __book_in_library(self, book_name: str, author: str):
        return book_name in self.books_available.get(author, [])

    def __is_rented(self, book_name: str):
        return any(book_name in user.keys() for user in self.rented_books.values())
