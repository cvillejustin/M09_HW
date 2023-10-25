import pandas as pd
import numpy as np

class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list = {'book_name':[], 'book_rating':[]}):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = pd.DataFrame(book_list)
        #self.num_books = len(self.book_list) if book_list is None else book_list

# can you, when creating an instance, also add a book/rating to the dataframe book_list or does it have to be added with the method
        
    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name'].unique():
            print("Book is already in your list!")
        else:
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
            })
            
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    
    
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
        
    def num_books_read(self):
        book_total = self.num_books
        print(book_total)
        
    def fav_books(self):
        fav_total = self.book_list[self.book_list.book_rating > 3]
        print(fav_total)

if __name__ == '__main__':

        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        print(test_object.book_list)
        test_object.add_book("War of the Worlds", 2)
        test_object.add_book("Shakespeare", 2)
        print(test_object.book_list)
        print(test_object.has_read("Star Trek"))
        print(test_object.has_read("Shakespeare"))
        test_object.num_books_read()
        test_object.fav_books()
