import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/mobile-phones-store"

response = requests.get(url)

if response.status_code == 200:
    body = response.text

    soup = BeautifulSoup(body, "html.parser")

    anchors = soup.find_all('a', class_="wjcEIp")

    for anchor in anchors:
        print(anchor.text)