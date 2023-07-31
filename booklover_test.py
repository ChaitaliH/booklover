from booklover import BookLover
import unittest
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1 = BookLover("Yuka Kawano", "ykawano@yahoo.com", "fiction")
        test1.add_book("Fault in our stars", 3)
        self.assertTrue(test1.has_read("Fault in our stars"))


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test1 = BookLover("Yuka Kawano", "ykawano@yahoo.com", "fiction")
        test1.add_book("Harry Potter", 5)
        test1.add_book("Harry Potter", 5)
        self.assertEqual(test1.add_book("Harry Potter", 5), test1.add_book("Harry Potter", 5))
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test1 = BookLover("Yuka Kawano", "ykawano@yahoo.com", "fiction")
        test1.add_book("Sherlock Holmes", 4)
        self.assertTrue(test1.has_read("Sherlock Holmes"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test1 = BookLover("Yuka Kawano", "ykawano@yahoo.com", "fiction")
        self.assertFalse(test1.has_read("The lord of the rings"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test1 = BookLover("Yuka Kawano", "ykawano@yahoo.com", "fiction")
        test1.add_book("War of the Worlds", 3)
        test1.add_book("Crash Landing", 5)
        test1.add_book("Alien in habitat", 4)
        self.assertEqual(test1.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test1 = BookLover("Yuka Kawano", "ykawano@yahoo.com", "fiction")
        test1.add_book("War of the Worlds", 3)
        test1.add_book("Crash Landing", 5)
        test1.add_book("Alien in habitat", 4)
        fav_books_df = test1.fav_books()
        self.assertTrue(fav_books_df['book_rating'].min() > 3)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)