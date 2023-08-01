my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_read(book_dictionary):
    book_string = f"This is the info of the book. Title: {book_dictionary['title']}\nAuthor: {book_dictionary['author']}\nYear: {book_dictionary['year']}\nRating: {book_dictionary['rating']}\nPages: {book_dictionary['pages']}"
    return book_string

# print(book_read(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_book_title(book_dictionary):
    return book_dictionary['title']
    
def get_book_author(book_dictionary):
    return book_dictionary['author']

def get_book_year(book_dictionary):
    return book_dictionary['year']

def get_book_rating(book_dictionary):
    return book_dictionary['rating']

def get_book_pages(book_dictionary):
    return book_dictionary['pages']

# print (get_book_title(my_book))
# print (get_book_author(my_book))
# print (get_book_year(my_book))
# print (get_book_rating(my_book))
# print (get_book_pages(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

my_library = [
    {
        "title": "Then Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.46,
        "pages": 309
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "rating": 4.25,
        "pages": 310
    },
]

def add_book(library, title, author, year, rating, pages):
    new_book ={
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    library.append(new_book)
    
def remove_book(library, title):
    for book in my_library:
        if book['title'] == title:
            my_library.remove(book)
            return
        
def search_book(library, title):
    for book in my_library:
        if book['title'] == title:
            return book
    return None

add_book(my_library, "How The Grinch Stole Christmas", "Dr. Seuss", "1957", "4.9", "64")
print("Books in the library:")
for book in my_library:
    print(f"Title: {book['title']}, Year: {book['year']}")

        
# remove_book(my_library, "How The Grinch Stole Christmas")
# for book in my_library:
#     print(f"Title: {book['title']}, Year: {book['year']}")

search_title = "How the Grinch Stole Christmas"
found_book = search_book(my_library, search_title)

if found_book:
    print(f"'{search_title}' found in the library:")
    print(f"Title: {found_book['title']}, Year:{found_book['year']}")
else:
    print(f"'{search_title}' not found in the library.")

