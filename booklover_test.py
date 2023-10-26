import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        book1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book1.add_book("War of the Worlds", 4)
        book = "War of the Worlds"
        self.assertTrue(book in book1.book_list['book_name'].unique(), "Your book was not added to the list")
        # add a book and test if it is in `book_list`.
    
    def test_2_add_book(self): 
        book1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book1.add_book("War of the Worlds", 4)
        book = "War of the Worlds"
        message = "Your book is in the list more than once"
        self.assertFalse(book1.book_list['book_name'].duplicated().any(), message)
        #Add the same book twice. Test if it's in book_list only once.

    def test_3_has_read(self):
        book1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book1.add_book("War of the Worlds", 4)
        book = "War of the Worlds"
        results = book1.has_read(book)
        message = "Your book is not in the list"
        self.assertTrue(results == True, message)
        #Pass a book in the list and test the answer is True.

    def test_4_has_read(self):
        book1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book1.add_book("War of the Worlds", 4)
        results = book1.has_read("new_book")
        test_value = True
        message = "Your book is in the list"
        self.assertFalse(results == test_value, message)
        #Pass a book NOT in the list and use assert False to test if the answer is True

    def test_5_num_books_read(self):
        book1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book1.add_book("Cat in the Hat", 3)
        book1.add_book("Green Eggs and Ham", 5)
        book1.add_book("War of the Worlds", 4)
        expected = 3
        #num_total = book1.num_books_read()
        message = "Your list does not have the expected number of books!"
        self.assertEqual(book1.num_books, expected, message)
        #Add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self): 
        book1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book1.add_book("Cat in the Hat", 3)
        book1.add_book("Green Eggs and Ham", 5)
        book1.add_book("War of the Worlds", 2)
        num_fav = book1.fav_books
        expected = 1
        self.assertTrue(num_fav, expected)
        #Add some books with ratings to the list, making sure some of them have rating > 3. 
        #Your test should check that the returned books have rating > 3.
                        
                        
if __name__ == '__main__':

    unittest.main(verbosity=3)