import bs4
from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as bSoup
myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient = uRequest(myUrl);
data = uClient.read();
uClient.close();
pageData = bSoup(data, "html.parser")

containers = pageData.find_all("div", {"class": "item-container"})
fileName = "products.csv"
f = open(fileName, "w")
header = "Brand, ProductName, shipping\n"
f.write(header)
print(pageData.h1)
# print(len(containers))
# print(containers[1].find("div", {"class": "item-info"}))


for container in containers:
    brand = container.find("div", {"class": "item-info"}).div.a.img["title"]
    titleContainer = container.findAll("a", {"class": "item-title"})
    productTitle = titleContainer[0].text
    shippingContainer = container.findAll("li", {"class": "price-ship"})
    shipping = shippingContainer[0].text.strip()
    print(brand)
    print(productTitle)
    print(shipping)
    f.write(brand+","+productTitle.replace(",", "|")+","+shipping+"\n")

