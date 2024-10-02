"""
Magic methdo

examples
 __init__
"""

class Book:
    def __init__(self, title, author, pages) -> None:
        self.__title = title
        self.__author = author
        self.__pages = pages

    def __repr__(self) -> str:
        return f'{self.__title} written by {self.__author}'
    
    def __str__(self):
        return self.__title
    
    def __len__(self):
        return self.__pages
    
book1 = Book('Python rocks!', 'My university', 300)
print(book1)
print(len(book1))