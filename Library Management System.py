class Book:
    def __init__(self, title, author, year, status=True):
        self._title = title
        self._author = author
        self._year = year
        self._status = status
    
    def displayData(self):

     print("Title:", self._title)
     print("Author:", self._author)
     print("Publication year :", self._year)
     print("Status:", self._status)



class Patron:
    def __init__(self, name, id, books,):
        self._name = name
        self._id = id
        self._books = books
        
    
    def displayData(self):

     print("Name:", self._name)
     print("ID:", self._id)
     print("Borrowed books:", self._books)
     


class Libary:
    def __init__(self, name, id, books,):
        self._
        self._
        self._
        
    
    def showBooks(self):

     print
     print
     print


e1 = Book ("War and Peace", "Leo Tolstoy", 1867, "True")

e1 = Patron ("Sean", "3422", "None")
e1.displayData()

b1 = Libary ("Samsung,", 1200)
b2 = Libary ("Apple,", 1800)
b3 = Libary ("Oppo,", 800)

b1.showBooks()
b2.showBooks()
b3.showBooks()
