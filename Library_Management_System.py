from dataclasses import dataclass
from typing import List 
import sys

# Python에서의 struct(구조체)는? -> StructedArray 
# -> Numpy 라이브러리를 사용해 구현할 수 있다.
@dataclass 
class Library: 
    book_name: List[chr] = None
    author: List[chr] = None
    pages: List[int] = None
    price: List[float] = None

library = Library()
library.book_name = []
library.author = []
library.pages = []
library.price = []

ar_nm = '' # 저자 이름

# 사용자 수, 서비스 선택, 책 개수
u = 0 
number = '' 
count = 0  
check = 0

while(number != '5'):
    print("Welcome to Library! \n")
    print("1. Add book information \n")
    print("2. Display book information \n")
    print("3. List all books of given author \n")
    print("4. List the count of books in the library \n")
    print("5. Exit \n")
    number = input("Enter one of the above: ")

    match number:
        case '1':
            library.book_name.append(input("Enter book name : "))
            library.author.append(input("Enter author name : "))
            library.pages.append(int(input("Enter Pages : ")))
            library.price.append(float(input("Enter price : ")))
            count += 1
        case '2':
            print("Okay. You have entered the following information \n")
            for i in range(count):
                print(f"book name : {library.book_name[i]}")
                print(f"\t author name : {library.author[i]}")
                print(f"\t pages : {library.pages[i]}")
                print(f"\t price : {library.price[i]}")
        case '3':
            ar_nm = input("Enter author name : ")
            for i in range(count):
                if ar_nm == library.author[i]:
                    print(library.book_name[i], library.author[i], library.pages[i], library.price[i], "\n")
                    check += 1
            if(check != 1):
                print("No results! Please try again.")  
        case '4':
            if count != 0:
                print(count)
            else:
                print("No of books in library \n")
        case '5':
            sys.exit("Program is End.")

