import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    body = response.text
    soup = BeautifulSoup(body, "html.parser")

    all_spans = soup.find_all('span', class_="text")

    for span in all_spans:
        print(span.text)
