# library_system.py

# Base Class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self):
        return f"'{self.title}' by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def get_details(self):
        return f"{super().get_details()} [EBook, {self.file_size}MB]"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author
