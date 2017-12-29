import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

count=0
filename = "Restaurants.csv"
f = open(filename, "w")
headers = "Place,Rating\n"
f.write(headers)
while(count<=200):
    my_url='https://www.yelp.com/search?find_desc=Restaurants&find_loc=Irvine,+CA&start='+str(count)
    #opening up connection, grabbing the page
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()

    #html parsing
    page_soup=soup(page_html,"html.parser")
    #grabs each product
    containers=page_soup.findAll("li",{"class":"regular-search-result"})



    for container in containers:
        restaurant_cont=container.findAll("div",{"class":"media-story"})[0]
        restName=restaurant_cont.findAll("a",{"class":"biz-name js-analytics-click"})[0].span.text
        restRate=restaurant_cont.findAll("div",{"class":"biz-rating biz-rating-large clearfix"})[0].div["title"]
        f.write(restName.replace(",","|") + ","+restRate+"\n")
        count+=1

f.close()