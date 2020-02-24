import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.amazon.co.jp/%E3%83%9E%E3%82%A4%E3%82%AF%E3%83%AD%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3-Sam-Newman/dp/4873117607', verify=False)

soup = BeautifulSoup(r.content, "html.parser")

print(soup.find("span", id="productTitle").text)
print(soup.find("span", class_="a-size-medium a-color-price offer-price a-text-normal").text)
