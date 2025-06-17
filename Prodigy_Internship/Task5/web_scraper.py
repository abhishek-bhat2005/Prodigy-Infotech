import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://books.toscrape.com/catalogue/page-1.html'

# CSV file to save
csv_file = open('books.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Price', 'Rating'])

while url:
    print(f"Scraping: {url}")

    # Get page content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # Get title
        title = book.h3.a['title']

        # Get price
        price = book.find('p', class_='price_color').text

        # Get rating
        rating_class = book.find('p')['class']
        rating = rating_class[1] if len(rating_class) > 1 else 'None'

        # Write to CSV
        csv_writer.writerow([title, price, rating])

    # Find next page
    next_button = soup.find('li', class_='next')
    if next_button:
        next_page = next_button.a['href']
        url = 'https://books.toscrape.com/catalogue/' + next_page
    else:
        url = None

csv_file.close()
print("Scraping completed! Data saved to books.csv")
