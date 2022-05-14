""" 
    
    Mya Nanmoo
    May 14, 2022
    whatabook.py
"""
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

""" DISPLAY MAIN MENU """
def displayMainMenu():

    print("\n -- WECOLME TO WHATABOOK --")
    print("\n  -- Main Menu --")
    print("\n 1. Books\n 2. Store Locations\n 3. My Account\n 4. Exit Program\n")


    mainMenu = ["1", "2", "3", "4"]
    choice = input(" PLEASE ENTER YOUR SELECTION! ")
    while choice not in mainMenu:
        print("\n** INVALID SELECTION: **")
        print("\n 1. Books\n 2.Store Locations\n 3. My Account\n 4. Exit Program\n")
        choice = input(" PLEASE ENTER YOUR SELECTION! ")
     

    if choice in mainMenu:
        validChoice = int(choice)
        return validChoice

""" DISPLAY BOOK LISTINGS """
def displayBooks(_cursor):

   
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    print("\n -- AVAILIABLE BOOK LISTINGS --\n")
    for b in books:
        print(f" Book Name: {b[1]}\n Book Author: {b[2]}\n".format(b[0], b[1], b[2]))
   
def displayLocations(_cursor):

    
    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()
    print("\n -- AVAILIABLE STORE LOCATIONS -- \n")
    for s in stores:
        print(f" Location: {s[1]}\n")



def validateUser():

    print("\n -- VIEW MY ACCOUNT --\n")

    
    user_id = ["1", "2", "3"]
    userID = input("PLEASE ENTER YOUR USER ID: ")
    while userID not in user_id:
        print("\n** INVALID USER ID. **\n")
        userID = input("PLEASE ENTER YOUR USER ID: ")
    
    if userID in user_id:
        validUserID = int(userID)
        return userID

""" DISPLAYING USER ACCOUNT MENU  """
def displayAccountMenu():

    print("\n-- USER ACCOUNT MAIN MENU --\n")
    print(" 1. Wishlist\n 2. Add A Book To  Wishlist\n 3. Main Menu\n")

    
    accountOptions = ["1", "2", "3", "4"]
    account_options = input("\n PLEASE ENTER YOUR SELECTION! ")

    
    while account_options not in accountOptions:
        print("\n** INVALID SELECTION: **")
        account_options = input("\n PLEASE ENTER YOUR SELECTION! ")
    
    if account_options in accountOptions:
        accountOptions = int(account_options)
        return accountOptions
def displayWishlist(_cursor, _user_id):
     
    Books = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
         
    _cursor.execute(Books)
    wishlistBooks= _cursor.fetchall()

    print("\n -- BOOKS ADDED TO WISHLIST-- \n")
    for b in wishlistBooks:
        print(f"\n Book ID: {b[0]}\n Book Name: {b[1]}\n Author: {b[2]}\n ")

""" ADDING BOOK TO WISHLIST """
def bookToWishlist(_cursor, _user_id, _book_id):

    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

""" DISPLAYING USER WISHLIST """
def displayWishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()


    print("\n -- DISPLAYING WISHLIST BOOKS --\n")
    for b in wishlist:
        print(f" Book Name: {b[4]}\n Author: {b[5]}\n")
try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    print("\n WELCOME TO WHATABOOK! ")
    mainMenu = displayMainMenu()
    while mainMenu< 4:
        
        if mainMenu== 1:
            displayBooks(cursor)    
        if mainMenu== 2:
            displayLocations(cursor)         
        if mainMenu== 3:
            userID = validateUser()
            accountOption = displayAccountMenu()
            while accountOption != 3:
                if accountOption == 1:
                    displayWishlist(cursor, userID)                       
                if accountOption == 2:
                    displayWishlist(cursor, userID)
                    bookID = input("\nEnter the Book ID you want to add to your wishlist! ")
                    validBookID = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while bookID not in validBookID:
                        print("\n** Invlaid Book ID. Please try again! **")
                        bookID = input("\nEnter the Book ID to add to wishlist! ")
                    if bookID in validBookID:
                        validBookID = int(bookID)
                    bookToWishlist(cursor, userID, validBookID)
                    db.commit()
                    print("\nYour Book was added successfully!")
                if accountOption == 4:
                    print("\nProgram Terminated....")
                    sys.exit()
                accountOption = displayAccountMenu()
            
        mainMenu = displayMainMenu()
        if mainMenu== 4:
            print("\nProgram Terminated....")
            sys.exit()
      

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()

