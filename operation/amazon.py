from logging import exception
import requests
import html5lib
from bs4 import BeautifulSoup
from utils.mongo import collection


def amaz(url):
    
    HEADER={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    
    r=requests.get(url, headers=HEADER)
    print(r.status_code)

    soup=BeautifulSoup(r.content, "html5lib")
    # print(soup.prettify())
    try:
        allbooks=soup.find_all("div", attrs={"class":"s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})

        for books in allbooks:
            #Title.....................................
            title=books.find("span", attrs={"class":"a-size-medium a-color-base a-text-normal"}).text
            # print(f"TITLE::{title}")
            

            #Price......................................
            b = books.find("span", attrs={"class":"a-price-whole"}) #We did it beacause some books don't have a price tag.
            if b:
                price= b.text
            
            # price=books.select_one(".template\=SEARCH_RESULTS > .s-card-border .s-price-instructions-style .a-price-whole").text  # We used css selector here.
            # print(f"PRICE:{price}")
            
            #Author.....................................
            # author=books.find("a", attrs={"a-size-base a-link-normal puis-light-weight-text s-underline-text s-underline-link-text s-link-style s-link-centralized-style"})

            author =books.select_one(".a-color-secondary .a-row .puis-light-weight-text+ .puis-light-w")
            
            if author:            
                aut= author.text
            else:
                aut= "Not Found"

            yield {"TITLE":title, "PRICE": price, "AUTHOR":aut}

    except exception as e:
        print(e)

        
    
page_no=1
while (page_no<=5):
    print(f"Pageeee no is:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {page_no}")
    url="https://www.amazon.in/s?k=books&page="+str(page_no)+"&crid=35KBWAK5YVV3F&qid=1664364280&sprefix=books%2Caps%2C212&ref=sr_pg_2"
    print(f"URL:{url}")
    a=amaz(url) 
    for i in a:
        # print(i)
        collection.insert_one(i)
    page_no=page_no+1