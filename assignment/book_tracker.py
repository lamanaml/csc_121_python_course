import csv


def dashboard():
    print("=" *40)
    print("📚  YOUR LIBRARY")
    print("=" *40)

def show_menu(library):
    response = input("\nWhat would you like to do? \n\n 1) View Books \n 2) Add a book \n\n q) Quit \n > ")
    response = response.lower().strip()
    if response == "1":
        view_book(library)
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

def view_book(library):
    #based on your comments, added a new function to view book.
    if len(library) > 0:
        # I feel like here I should have used the index of the item in the library 
        # (i = i +1, but I tried several ways and could not get it to work), so I took the easy way out.
        number = 1
        for book in library:
            # print(f"{num}. '{book['title']}' - {book['author']} ({book['pages']} pages - approx. {book['hours']} hours to read) ")
            print(format_book(book, number))
            number = number + 1 
    else:
        print("Your library is empty. Add a book first!")
    show_menu(library)
    
def save_book(book):
    with open("books.csv", "a", newline="") as book_new:
        writer = csv.DictWriter(book_new, fieldnames=["title","author","pages","hours"] )
        writer.writerow(book)  

def load_books(library):
    with open("books.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            library.append(row)
    return

        
        # for book in sorted(books, key=lambda student: student["name"]):
        #print(f"{student['name']} is in {student['home']}")
        
def add_book(library):
    #get user input for title, author and page count.  Create a variable called hours that calls the function estimate_reading_time
    title = input("What is the Book Title? ")
    author = input("Who is the Author? ")
    pages = int(input("How many pages? "))
        #need something here to say if page is not a number, "enter a number"
    hours =  float(estimate_reading_time(pages))
    
    book = {
        "title": title.title(), 
        "author": author.title(), 
        "pages": pages, 
        "hours": hours 
        } 
    library.append(book)
    print(f"Your book has been submitted\n___________")
    print(f"Book Title: {title}\nAuthor: {author}\nPage Count {pages}")
    print(f"\nBook Added:\n")
    print(format_book(book, len(library)))
    save_book(book) 
    show_menu(library)

def format_book(book, number):
    # return an f-string using number, book["title"], book["author"],
    # book["pages"], and book["hours"] in the format shown above
    return (
        f"{number}. '{book['title']}' - {book['author']} "
        f"({book['pages']} pages - approx. {book['hours']} hours to read)"
    )
         
def main():
    library = []
    load_books(library)
    dashboard()
    show_menu(library)
   
    
    
if __name__ == "__main__":
    main()