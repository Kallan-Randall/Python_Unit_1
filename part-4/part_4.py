### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# fave_book = input("What is your favorite book? ")
# title = input('What is the title of the book you would like to add? - ')
# author = input('Who is the author of the book you would like to add? - ')
# year = input('What year was the book published? - ')
# rating = input('What rating out of 5 would you give this book? - ')
# pages = input('What is the page count of the book? - ')


# def create_new_book():
#     title = input('What is the title of the book you would like to add? - ')
#     author = input('Who is the author of the book you would like to add? - ')
#     year = input('What year was the book published? - ')
#     rating = input('What rating out of 5 would you give this book? - ')
#     pages = input('What is the page count of the book? - ')
    
#     print(f"Type of 'title': {type(title)}")
    
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
    
#     return book_dictionary

# create_new_book()



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():
#     title = input('What is the title of the book you would like to add? - ')
#     author = input('Who is the author of the book you would like to add? - ')
#     year = int(input('What year was the book published? - '))
#     rating = float(input('What rating out of 5 would you give this book? - '))
#     pages = int(input('What is the page count of the book? - '))
   
#     print(f"Type of 'title': {type(title)}")
    
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
    
#     return book_dictionary

# create_new_book()

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def create_new_book():
#     title = input('What is the title of the book you would like to add? - ')
#     author = input('Who is the author of the book you would like to add? - ')
#     # year
#     try:
#         year = int(input('What year was the book published? - '))
#     except:
#         year = int(input('Please type a number for the year - '))
#     # rating
#     try:
#             rating = float(input('What rating out of 5 would you give this book? - '))
#     except:
#             rating = float(input('please type a number for the rating - '))
#     # pages
#     try:
#         pages = int(input('What is the page count of the book? - '))
#     except:
#         pages = int(input('Please type a number - '))
        
#     print(f"Type of 'title': {type(title)}")
    
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
    
#     return book_dictionary

# create_new_book()

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

book_library = [
    {
        "title": "Fellowship of the ring",
        "author": "JRR Tolkien",
        "year": "1954",
        "rating": "4.7",
        "pages": "432"
    },
    {
        "title": "The Two Towers",
        "author": "JRR Tolkien",
        "year": "1954",
        "rating": "4.7",
        "pages": "352"
    },
    {
        "title": "Return of the King",
        "author": "JRR Tolkien",
        "year": "1955",
        "rating": "4.9",
        "pages": "464"
    }
]

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
    
    book_library.append(book_dictionary)
    
def see_all_books():
    for book in book_library:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")


def search_book():
    title_search = input("Enter the title of the book you would like to search. - ")
    found_book = None
    
    for book in book_library:
        if book['title'] == title_search:
            found_book = book
            break
    if found_book:
        print('Book Found!')
        print(f"Title: {found_book['title']}, Author: {found_book['author']}, Year: {found_book['year']}, Rating: {found_book['rating']}, Pages: {found_book['pages']}")
    else:
        print("Book not found in library")

def main_menu():
    print("Main Menu")
    print("1. Add new book")
    print("2. See all books")
    print("3. Search for a book")
    print("4. Exit")


main_menu()
choice = input("Enter the number for desired choice - ")

if choice == "1":
    add_new_book()
elif choice == "2":
    see_all_books()
elif choice == "3":
    search_book()
elif choice == "4":
    print("exiting program.")
else:
    print("Not valid option. Select 1-4")





### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

while True:
    main_menu()
    choice = input("Enter the number for desired choice - ")

    if choice == "1":
        add_new_book()
    elif choice == "2":
        see_all_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("exiting program.")
        break
    else:
        print("Not valid option. Select 1-4")
        
        
if __name__ == "__main__":
    main_menu()