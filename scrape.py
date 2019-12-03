import requests 
from bs4 import BeautifulSoup 
import pandas as pd

# get URL
URL = "https://www.nytimes.com/interactive/2019/books/notable-books.html"
r = requests.get(URL) 

# Parse URL using html5lib parser
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 

# Get div section having class g-books from HTML
table = soup.find('div', attrs = {'class':'g-books'}) 
print(table.prettify()) 

# Create empty list to store books' info
books = []

# Iterate through all entries in table
for row in table.findAll('div', attrs = {'class':'g-book'}):
    
    # Create empty dictionary to store book properties
    book = {}
    
    book['title'] = row.find('div',attrs = {'class':'g-book-title'}).a.text.strip() # get title
    book['author'] = row.find('div',attrs = {'class':'g-book-author'}).b.text.strip() # get author
    book['desc'] = row.find('div',attrs = {'class':'g-book-description'}).text.strip() # get desc
    
    # get multiple genres in a list
    tags = row.find('div', attrs = {'class':'g-book-tags'})   
    genres = []
    for tag in tags.findAll('span', attrs = {'class':'g-book-tag'}):
        genre = tag.text.strip()[:-1]
        genres.append(genre)
    
    
    book['genre'] = genres # get genres
    
    # Append dictionary of book properties to list
    books.append(book)

# Store list as a table
df_books = pd.DataFrame(books)
df_books = df_books[['title','author','desc','genre']]