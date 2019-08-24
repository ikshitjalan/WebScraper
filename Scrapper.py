from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.amazon.in/s?i=stripbooks&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A15417300031%2Cn%3A4149418031%2Cn%3A4149470031&lo=list&qid=1566635005&ref=sr_pg_1").text

soup = BeautifulSoup(source,"lxml")

csv_file = open("BookARead.csv",'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image','Title','Price','Rating','Author'])

try:
    for product in soup.findAll("div", {"class": "s-item-container"}):
        image = product.find("div",{"class":"a-column a-span12 a-text-center"}).a.img["src"]
        print("Image:",image)
        title = product.find("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})["title"]
        print("Title:",title)
        price = product.findAll("div",{"class":"a-row a-spacing-none"})[3].a.text
        print("Price:",price)
        rating = product.find("div",{"class":"a-column a-span5 a-span-last"}).i.span.text
        print("Rating:",rating)
        try:
            author = product.findAll("div",{"class":"a-row a-spacing-none"})[1].a.text
            
        except Exception as e:
            author = product.findAll("span",{"class":"a-size-small a-color-secondary"})[2].text
        print("Author:",author)
        print()
        csv_writer.writerow([image,title,price,rating,author])
except Exception as i:
    pass

csv_file.close()
