# # libery management system 
# #(register login   -> user)
# (add book , issue book , return book,view book ,search book)

#creating two file names user.txt and book.txt to store user information and book information permanently inside the file 

import os 

if not os.path.exists('users.txt'):
    with open('users.txt',"w") as f:
        pass
if not os.path.exists('books.txt'):
    with open('books.txt',"w") as f:
        pass

#load data from the file
def load_user():
    users_dict = {}

    try:
        with open('users.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(',')
                    users_dict[username] = password
    except FileNotFoundError:
        print("users.txt not found")

    return users_dict

def load_books():
    books_list = []
    try:
        with open("books.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id, title, author, quantity = line.split(',')

                    book = {
                        'id' : book_id,
                        'title' : title,
                        'author' : author,
                        'quantity' : int(quantity)
                    }
                    books_list.append(book)
    except FileNotFoundError:
        print("file not found!")
    return books_list

def get_existing_books_id(books_list):
    """Create a set to store all the ids of the booksa"""
    book_ids = set()
    for book in  books_list:
        #dict aauchha
        book_ids.add(book['id'])
    return book_ids

#user register
def register_user(users_dict):
    """register a new user"""
    print("\n---Register a New User---")
    username = input("Enter the username: ").strip()
    password = input("Enter the password:").strip()
    if username in users_dict:
        print(f"usernamae already exists!")
        return False
    if not username or not password:
        print("Username and password cannot be empty")
        return False
    users_dict[username] = password 

    #save the register user to the file 'users.txt'
    with open('users.txt','a') as f:
        f.write(f"{username},{password}\n")
        print("registeration sucessfully")
        return True
    
# users_dict = load_user()
# print(users_dict)
# register_user(users_dict)

def login_user(users_dict):
    print("\n----Login User----")
    username = input("Enter username:").strip()
    password = input("ENter password:").strip()

    if username in users_dict and users_dict[username] == password:
        print(f"Welcome!{username.capitalize()}")
        return username
    else: 
        print("Invalid username or password!")
        return None
        
# login_user(users_dict)

#now book khuleawo
# main menu function
def main_menu():
    """Display main menu options"""
    print("="*55)
    print("\n Libary Management system")
    print("="*55)
    print("1.Add Book")
    print("2. View all books")
    print("3. search Book")
    print("4. Issue Books")
    print("5. Return Book")
    print("6. Logout")
    print("="*55)

    #main_menu()

    #add book
def add_book(books_list,books_ids):
        """Add a new book to the library"""
        print("\n ----Add New book----")
        book_id = input("Enter the Book ID:").strip()


        if book_id in books_ids:
            print("Book id already exist!")
            return
        
        title = input("Enter the book title:").strip()
        author = input("Enter the author:").strip()
        quantity = int(input("Enter the quantity:").strip())

        new_book = {
            'id':book_id,
            'title': title,
            'author': author,
            'quantity': quantity
        }

        books_list.append(new_book)
        book_ids.add(book_id)

        with open('books.txt', 'a') as f:
            f.write(f"{book_id},{title},{author},{quantity}\n")

        print("Book added sucessfully")

# books_list = load_books()
# book_ids = get_existing_books_id(books_list)
# print(books_list)
# print(book_ids)
# add_book(books_list ,book_ids)
 
###Function to view all the books in the library
def view_books(books_list):
    """Display all the books in the library"""
    print("\n----All book in the library----")
    if not books_list:
        print("No boooks found i library!")
        return
    for book in books_list:
        print(f"{book['id']} | {book['title']} | {book['quantity']}")
# view_books(books_list)

### todayyy dAY 3
###search a book using title or author
def search_book(books_list):
    found_items = []
    """search book by author name or booktitle"""
    search_term = input("search here:").strip().lower()

    for book in books_list:
        if search_term in book['title'] or search_term in book['author']:
            found_items.append(book)

    if found_items:
        print(f"Found {len(found_items)} books")
        view_books(found_items)

    else:
        print("No books available")

    #search_books(books_list)


#save books to the file
def save_books(books_list):
    """write all books bac:k to books.txt"""
    with open("books.txt", "w") as f:
        for book in books_list:
            f.write(f"{book['id']}, {book['title']}, {book['author']},{book[quantity]}")

###Issue book-> user le book lanu libary bata
def issue_book(books_list):
    book_id = input("Enter the book id to issue:").strip()

    for book in books_list:
        if book['id'] == book_id:
            if book['quantity'] > 0:
                book['quantity'] -= 1

                save_books(books_list)
                print(f"Book {book['title']} issued sucessfully!")
                print(f"remaining quantity: {book['quantity']}")

            else:
                print("Book is currenntly out of stoke!")
                return
    print("Book id not found")
def return_book(books_list):
    """Return abook to a user"""
    book_id = input("Enter the book id to return:").strip()
    for book in books_list:
        if book['id'] == book_id:
            book['quanity'] += 1

            save_books(books_list)

            print(f"Book {book['title']} returned sucessfully!")
            print(f"Current quality: {book['quantity']}")
            return
        
    print("Book id not found")
# add_book(books_list, book_ids)
# issue_book(books_list)
# return_book(books_list)

### Main function ---> control overal program flow
def main():
    "Main program loop"
    user_dict = load_user()

    print("="*50)
    print("----Welcome to library Management system----")
    print("="*50)

    while True:
        print("\n 1. Register")
        print("\n 2. Login")
        print("\n 3. Exist")

        choice = input("\n ENter choice(1,2,3):")

        if choice == '1':
            register_user(user_dict)
        elif choice == '2':
            username = login_user(user_dict)

            if username:
                books_list = load_books()
                book_ids = get_existing_books_id(books_list)

                while True:
                    main_menu()
                    menu_choice = input("\n Enter the choice (1-6):")
                    if menu_choice == '1':
                        add_book(books_list,book_ids)
                    elif menu_choice == '2':
                        view_books(books_list)
                    elif menu_choice == '3':
                        search_book(books_list)
                    elif menu_choice == '4':
                        issue_book(books_list)
                    elif menu_choice == '5':
                        return_book(books_list)
                    elif menu_choice == '6':
                        print(f"Bye {username.capitalize()}")
                        break
                    else:
                        print("Invslid choice")

        elif choice == '3':
            print(" keep visiting ")

        

if __name__ == "__main__":
    main()





















