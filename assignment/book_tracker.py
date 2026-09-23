def dashboard():
    print("=" *40)
    print("📚  YOUR LIBRARY")
    print("=" *40)

def show_menu(library):
    response = input("\nWhat would you like to do? \n\n 1) View Books \n 2) Add a book \n\n q) Quit \n > ")
    response = response.lower().strip()
    if response == "1":
        if len(library) > 0:
            # I feel like here I should have used the index of the item in the library 
            # (i = i +1, but I tried several ways and could not get it to work), so I took the easy way out.
            num = 1
            for book in library:
                print(f"{num}. '{book['title']}' - {book['author']} ({book['pages']} pages - appox. {book['hours']} hours to read) ")
                num = num + 1
                show_menu(library)
        else:
            print("Your library is empty. Add a book first!")
            show_menu(library)
    elif response == "2":
        add_book(library) 
    elif response == "q" or response == "quit" or response == "exit":
        print("Goodbye!")
        return
        
    else:
         print("pick 1, 2 or q")
         print("Sorry, that option isn't available.")
         show_menu(library) 
  
def estimate_reading_time(pages):
    # estimated reading time in hours, assuming 40 pages/hour.  
    # This number should be rounded to 1 decimal place
    return round(pages / 40, 1)

def add_book(library):
    #get user input for title, author and page count.  Create a variable called hours that calls the function estimate_reading_time
    title = input("What is the Book Title? ")
    author = input("Who is the Author? ")
    pages = int(input("How many pages? "))
        #need something here to say if page is not a number, "enter a number"
    hours =  estimate_reading_time(pages)
    
    book = {
        "title": title.title(), 
        "author": author.title(), 
        "pages": pages, 
        "hours": hours 
        } 
    library.append(book)
    print(f"Your book has been submitted\n___________")
    print(f"Book Title: {book['title']}\nAuthor: {book['author']} \nPage Count {book['pages']}")
    print(f"\nBook Added:\n")
    print(f"'{book['title']}', by {book['author']} -- appox. {book['hours']} hours to read) ")
    show_menu(library)
         
def main():
    library = []
    dashboard()
    show_menu(library)
    
    
    
    
if __name__ == "__main__":
    main()