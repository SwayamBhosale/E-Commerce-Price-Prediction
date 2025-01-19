import requests
from bs4 import BeautifulSoup
import csv

def scrape_data():
    url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    products = []
    for product in soup.find_all("div", class_="cPHDOP col-12-12"):
        name = product.find("div", class_='KzDlHZ').text if product.find("div", class_='KzDlHZ') else "N/A"
        price = product.find("div", class_="Nx9bqj _4b5DiR").text.replace("₹", "") if product.find("div", class_="Nx9bqj _4b5DiR") else "N/A"
        rating = product.find("div", class_="XQDdHH").text if product.find("div", class_="XQDdHH") else "N/A"
        products.append([name, price, rating])
    
    with open("ecommerce_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating"])
        writer.writerows(products)
    
    print("Data scraped and saved to ecommerce_data.csv")

if __name__ == "__main__":
    scrape_data()