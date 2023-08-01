### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["J.R.R Tolkien", "J.K. Rowling", "Stephen King", "C.S. Lewis", "James Patterson", "Tom Clancy", "Dr. Seuss"]
# print(my_authors)


# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append("H.G. Wells")
# print(my_authors)

# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove("H.G. Wells")
# print(my_authors)


# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
# print(my_authors[3])

# Now slice the list.

# Code here
# Example: my_authors[1:4]
my_authors[1:3]
# print(my_authors[1:3])


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
tuple_author = ("J.R.R Tolkien", "J.K. Rowling", "Stephen King", "C.S. Lewis", "James Patterson", "Tom Clancy", "Dr. Seuss")

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
set_author = {"J.R.R. Tolkien", "J.K. Rowling", "Stephen King", "C.S. Lewis", "James Patterson", "Tom Clancy", "Dr. Seuss"}

# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
set_author.add("Jan Berenstain")
# print(set_author)
# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
set_author.add("Jan Berenstain")
# print(set_author)


### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# List
for author in my_authors:
    print(author)

# tuple
for author in tuple_author:
    print(author)

# set
for author in set_author:
    print(author)

# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

