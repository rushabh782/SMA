import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

products = soup.find_all("li",attrs={"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

bookList = []

for item in products:
    bookObj = {}
    bookObj['title'] = item.find("h3").find("a").get("title")
    bookObj['cover'] = url + item.find("img",attrs={"class":"thumbnail"}).get("src")
    bookObj['rating'] = item.find("p",attrs={"class":"star-rating"}).get("class")[1]
    bookObj['price'] = item.find("p",attrs={"class":"price_color"}).text
    
    bookList.append(bookObj)
    
    df = pd.DataFrame(bookList)
df.to_csv("books.csv",index=False)