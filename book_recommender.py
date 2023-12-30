import pandas as pandas
import requests
from bs4 import BeautifulSoup
import random
import re

base_url = "https://www.goodreads.com/"

def clean_text(text):
    cleaned_text = ' '.join(text.split())
    cleaned_text = re.sub(r'\.([A-Z])', r'. \1', cleaned_text)
    cleaned_text = cleaned_text.replace(" . . .", "...").replace(". . .", "...")
    return cleaned_text

def scrape_book_desc(book_url):
    response = requests.get(book_url).text
    soup = BeautifulSoup(response, "html.parser")
    desc = soup.find("div", {"data-testid": "description"})
    if desc:
        return clean_text(desc.text)
    return None

def italicize(text):
    return f"*{text}*"

def generate_book_recommendation(genre):
    if len(genre.split()) == 2:
        words = genre.split()
        genre = "-".join(words)
    page_url = f"{base_url}shelf/show/{genre}"
    response = requests.get(page_url).text

    soup = BeautifulSoup(response, "html.parser")
    books = soup.find_all("div", "elementList")

    if not books:
        print("Hmm, couldn't find any books for this genre. Try again?")
        return

    book_num = random.randint(0,49)
    chosen_book = books[book_num]

    title = chosen_book.find("a", "bookTitle").text
    author = chosen_book.find("a", "authorName").text
    book_url = base_url + chosen_book.find("a", "bookTitle").get("href")
    formatted_url = f"<{book_url}>"
    desc = scrape_book_desc(book_url)

    return(f"Your newest {genre} read just landed...\n\n{italicize('Title')}: {title}\n{italicize('Author')}: {author}\n{italicize('Description')}: {desc}\n{italicize('Check it out:')} {formatted_url}\n\nHappy reading! <3")

