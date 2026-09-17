def dashboard():
    print("=" *40)
    print("📚  YOUR LIBRARY")
    print("=" *40)
    
def estimate_reading_time(pages):
    # estimated reading time in hours, assuming 40 pages/hour.  
    # This number should be rounded to 1 decimal place
    return round(pages / 40, 1)

def add_book():
    #get user input for title, author and page count.  Create a variable called hours that calls the function estimate_reading_time
    title = input("What is the Book Title? ")
    author = input("Who is the Author? ")
    pages = int(input("How many pages? "))
    hours =  estimate_reading_time(pages)
    print(f"Your book has been submitted\n___________")
    print(f"Book Title: {title}\nAuthor: {author}\nPage Count {pages}")
    print(f"\nBook Added:\n")
    print(f"  '{title}' by {author} -- approx. {hours} hours to read")
        
def main():
    add_book()
    dashboard()
    
if __name__ == "__main__":
    main()