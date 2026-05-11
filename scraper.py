import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "http://books.toscrape.com/"

# Send request
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

# Lists to store data
names = []
prices = []
ratings = []

# Find all books
books = soup.find_all("article", class_="product_pod")

for book in books:
    # Name
    name = book.h3.a["title"]
    
    # Price
    price = book.find("p", class_="price_color").text
    
    # Rating
    rating = book.find("p")["class"][1]
    
    names.append(name)
    prices.append(price)
    ratings.append(rating)

# Create DataFrame
data = pd.DataFrame({
    "Name": names,
    "Price": prices,
    "Rating": ratings
})

# Save to CSV
data.to_csv("products.csv", index=False, encoding="utf-8")

print("✅ Data saved to products.csv")
print(data)