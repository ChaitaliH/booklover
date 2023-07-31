import pandas as pd
import numpy as np

class BookLover:
    
    #constructor
    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    #Method 1
    def add_book(self, book_name, book_rating):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f"{self.name} has already read '{book_name}'.")

    
    #Method 2        
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    #Method 3
    def num_books_read(self):
        return self.num_books
    
    #Method 4
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    
    test_object1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object1.add_book("War of the Worlds", 4)