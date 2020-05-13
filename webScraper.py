from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get('https://realpython.com/best-python-books/')
beauty = BeautifulSoup(response.text, 'html.parser')

books = beauty.find_all(class_='section3')

with open('books.csv', 'w') as csv_file:
    csv_writer=writer(csv_file)
    headers = ['Title', 'Author', 'Link']
    csv_writer.writerow(headers)

    for book in books:
        title = book.find('h3').get_text().replace('\n', '')
        author = book.find('p').get_text().replace('\n', '')
        link = book.find('a')['href'].replace('\n', '')
        csv_writer.writerow([title, author, link])
