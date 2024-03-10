import math
import numpy as np
import os 
import sys


# CMD Commands
# To install Snakeviz Python Profiler: python -m pip install snakeviz --user
# To generate profile: python -m cProfile -o program.prof program_to_profile.py
# To view profile after generated: python -m snakeviz program.prof

class Book:
    def __init__(self, name: str, author: str, date: str, publisher: str, number_of_pages: int):
        self.name = name
        self.author = author
        self.date = date
        self.publisher = publisher
        self.number_of_pages = number_of_pages

    def __str(self):
        return f'The book is {self.name}, \nThe author is {self.author}'

    def get_book_info(self):
        print('Information about the book:')
        print(f'Book name: {self.name}')
        print(f'Book author: {self.author}')
        print(f'Book release date: {self.date}')
        print(f'Book publisher: {self.publisher}')
        print(f'Book number of pages: {self.number_of_pages}')

    def dummy_function(self):
        for i in range(10000):
            print(i**5)

if __name__ == "__main__":
    dataset = {
        'book1': {'name': 'Apples', 'author': 'Sam', 'date': '2022', 'publisher': 'ps1', 'number_of_pages': 100},
        'book2': {'name': 'Fruits', 'author': 'Amy', 'date': '2021', 'publisher': 'ps2', 'number_of_pages': 600},
        'book3': {'name': 'Cars', 'author': 'Carl', 'date': '2020', 'publisher': 'ps2', 'number_of_pages': 500},
        'book4': {'name': 'Cities', 'author': 'Peter', 'date': '1922', 'publisher': 'ps2', 'number_of_pages': 200}
    }

    books = []

    for book in dataset.values():
        e = Book(book['name'], book['author'], book['date'], book['publisher'], book['number_of_pages'])
        books.append(e)

    books[0].get_book_info()
    books[0].dummy_function()


