from project.user import User
from project.library import Library

class Registration:

    def __init__(self):
        pass
    @staticmethod
    def add_user(user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        user = [user for user in library.user_records if user.user_id == user_id]
        if not user:
            return f"There is no user with id = {user_id}!"
        user = user[0]
        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        user.username = new_username
        data = library.rented_books.get(user.username)
        if data:
            del library.rented_books[user.username]
            library.rented_books[new_username] = data
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
