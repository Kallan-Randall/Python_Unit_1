### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
# def add_new_book():
#     title = input("Enter the title of the new book: ")
#     author = input("Enter the name of the author: ")
#     year = int(input("Enter the Year the book was published: "))
#     rating = float(input("Enter rating of book: "))
#     pages = int(input("Enter number of pages: "))
    
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
        
#     with open("book_library.txt", "a") as f:
#         f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


# add_new_book()
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
# def see_all_books():
#     with open("book_library.txt", "r") as f:
#         file = f.readlines()
        
#     for line in file:
#         title, author, year, rating, pages = line.split(", ")
        
#         book_dictionary = {
#             "title": title,
#             "author": author,
#             "year": int(year),
#             "rating": float(rating),
#             "pages": int(pages)
#         }
        
#         print(f"Title: {book_dictionary['title']}, Author: {book_dictionary['author']}, year: {book_dictionary['year']}, rating: {book_dictionary['rating']}, pages: {book_dictionary['pages']}")
    
# see_all_books()
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.
# def main_menu():
#     while True:
#         print("Main Menu:")
#         print("1. Add a new book")
#         print("2. See all books on the shelf")
#         print("3. Search for a book by title")
#         print("4. Exit")

#         choice = input("Enter the number corresponding to your choice: ")

#         if choice == "1":
#             add_new_book()
#         elif choice == "2":
#             see_all_books()
#         # elif choice == "3":
#         #     search_book_by_title()
#         elif choice == "4":
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid option. Please enter a valid choice (1-4).")
# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def add_new_book():
    title = input("Enter the title of the new book: ")
    author = input("Enter the name of the author: ")
    year = int(input("Enter the Year the book was published: "))
    rating = float(input("Enter rating of book: "))
    pages = int(input("Enter number of pages: "))
    
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
        
    with open("book_library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

def see_all_books():
    with open("book_library.txt", "r") as f:
        file = f.readlines()
        
    for line in file:
        title, author, year, rating, pages = line.split(", ")
        
        book_dictionary = {
            "title": title,
            "author": author,
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages)
        }
        
        print(f"Title: {book_dictionary['title']}, Author: {book_dictionary['author']}, year: {book_dictionary['year']}, rating: {book_dictionary['rating']}, pages: {book_dictionary['pages']}")
    
def search_book_title():
    title_to_search = input("Enter the name of the book: ")
    
    with open("book_library.txt", "r") as f:
        file = f.readlines()
        
    found_books = []
    for line in file:
        title, author, year, rating, pages = line.strip().split(", ")
        if title.lower() == title_to_search.lower():
            book = {
                'title': title,
                "author": author, 
                "year": int(year), 
                "rating": float(rating),
                "pages": int(pages)
            }
            found_books.append(book)
    
    if found_books:
        print("Found book:")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating1']}, Pages: {book['pages']}")
    else:
        print(f"No books found with title: {title_to_search}")

def search_book_author():
    author_to_search = input("Enter the name of the author: ")
    
    with open("book_library.txt", "r") as f:
        file = f.readlines()
        
    found_books = []
    for line in file:
        title, author, year, rating, pages = line.strip().split(", ")
        if author.lower() == author_to_search.lower():
            book = {
                'title': title,
                "author": author, 
                "year": int(year), 
                "rating": float(rating),
                "pages": int(pages)
            }
            found_books.append(book)
    
    if found_books:
        print("Books by author:")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")
    else:
        print(f"No books found by: {author_to_search}")
        
        
def page_count():
    total_pages = 0
    
    with open("book_library.txt", "r") as f:
        file = f.readlines()
        
        for line in file:
            _,_,_,_,pages = line.strip().split(", ")
            total_pages += int(pages)
        print(f"Total Number of pages in library: {total_pages}")

def total_books_in_library():
    with open("book_library.txt", "r") as f:
        num_books = len(f.readlines())
    
    print(f"Total number of books in library: {num_books}")


def main_menu():
    while True:
        print("Main Menu:")
        print("1. Add a new book")
        print("2. See all books on the shelf")
        print("3. Search for a book by title")
        print("4. Search for a book by author")
        print("5. Total pages in library")
        print("6. Total number of books in the library")
        print("7. Exit")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            add_new_book()
        elif choice == "2":
            see_all_books()
        elif choice == "3":
            search_book_title()
        elif choice == "4":
            search_book_author()
        elif choice == "5":
            page_count()
        elif choice == "6":
            total_books_in_library()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter a valid choice (1-7).")




if __name__ == "__main__":
    main_menu()