from typing import Container
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


constainers = page_soup.find_all("div", {"class": "_4ddWXP"})
# print(len(constainers))


# print(soup.prettify(constainers[0]))
container = constainers[0]
print(container.div.img["alt"])


price = container.find_all("div", {"class": "_30jeq3"})
print(price[0].text)

filename = "products.csv"
f = open(filename, "w")

headers = "Product_Name, Pricing"
f.write(headers)

for container in constainers:
    product_name = container.div.img["alt"]

    price_container = container.find_all("div", {"class": "_30jeq3"})
    price = price_container[0].text.strip()

    print("product_name:" + product_name)
    print("price:" + price)

    f.write(product_name + price)

f.close()