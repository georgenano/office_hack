import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.amazon.co.jp/'\
        '%E3%83%9E%E3%82%A4%E3%82%AF%E3%83%AD%E3%82%B5%E3%83%BC%E3%83%93'\
        '%E3%82%B9%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3'\
        '-Sam-Newman/dp/4873117607'
    book = getBookInfo(url)
    print('title:' + book.title)
    print('price:' + book.price)
    print('isbn:' + book.isbn)


class BookInfo:
    def __init__(self, title, price, isbn):
        self.title = title
        self.price = price
        self.isbn = isbn


def getBookInfo(url):
    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, "html.parser")

    title = soup.find("span", id="productTitle").text
    price = soup.find("span", class_="a-size-medium a-color-price offer-price a-text-normal").text.strip('￥')
    isbn = soup.find(text='ISBN-10:').parent.parent.contents[1].strip(' ')

    book = BookInfo(title, price, isbn)
    return book


if __name__ == '__main__':
    main()