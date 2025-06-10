import requests
from bs4 import BeautifulSoup

city = input("Enter city name: ")

url = f"https://timesofindia.indiatimes.com/city/{city}"

response = requests.get(url)

if response.status_code == 200:
    body = response.text

    soup = BeautifulSoup(body, "html.parser")

    anchors = soup.find_all('a', class_="linktype1")

    for anchor in anchors[:5]:
        print(anchor.text)