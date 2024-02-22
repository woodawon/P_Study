from dataclasses import dataclass
from typing import List 

# Python에서의 struct(구조체)는? -> StructedArray 
# -> Numpy 라이브러리를 사용해 구현할 수 있다.
@dataclass 
class Library: 
    book_name: List[chr] = None
    author: List[chr] = None
    pages: List[int] = None
    price: List[float] = None

library = Library()
ar_nm = List[chr]
bk_nm = List[chr]

# 사용자 수, 서비스 선택, 책 개수
u = 0 
number = 0 
count = 0  

while(number != 5):
    print("Welcome to Library! \n")
    print("1. Add book information \n")
    print("2. Display book information \n")
    print("3. List all books of given author \n")
    print("4. List the count of books in the library \n")
    print("5. Exit \n")
    number = input("Enter one of the above: ")

    match (number):
        case (1):
            library.book_name.add(input("Enter book name : "))
            library.author.add(input("Enter author name : "))
            library.pages.add(input("Enter Pages : "))
            library.price.add(input("Enter price : "))
        case (2):
            print("Fizz")
        case (3):
            print("Buzz")
        case (4):
            print("Buzz")
        case (5):
            sys.exit("Program is End.")

