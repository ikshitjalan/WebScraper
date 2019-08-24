from bs4 import BeautifulSoup
import requests
import csv

# source = requests.get("https://www.amazon.in/s?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A15417300031%2Cn%3A4149418031%2Cn%3A4149470031&page=2&qid=1566657825&ref=lp_4149470031_pg_2").text
source = requests.get("https://www.amazon.in/s?i=stripbooks&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A15417300031%2Cn%3A4149418031%2Cn%3A4149470031&page=3&qid=1566664538&ref=sr_pg_3").text

soup = BeautifulSoup(source,"lxml")

csv_file = open("BookARead.csv",'w',encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image','Title','Price','Rating','Author'])

try:
    for product in soup.findAll("div", {"class": "s-include-content-margin s-border-bottom"}):
        image = product.find("div",{"class":"a-section aok-relative s-image-fixed-height"}).img["src"]
        print("Image:",image)
        title = product.find("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"}).a.span.text
        print("Title:",title)
        price = product.find("span",{"class":"a-offscreen"}).text
        print("Price:",price)
        rating = product.find("a",{"class":"a-popover-trigger a-declarative"}).i.span.text
        print("Rating:",rating)
        try:
            author = product.find("div",{"class":"a-row a-size-base a-color-secondary"}).a.text
        except Exception as e:
            author = product.findAll("span",{"class":"a-size-base"})[1].text
    
            
        print("Author:",author)
        print()
        csv_writer.writerow([image,title,price,rating,author])


except Exception as i:
    pass

csv_file.close()
