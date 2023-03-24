import requests
from bs4 import BeautifulSoup
product_code = input("Podaj kod produktu: ")
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
if response.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(response.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    print(type(opinions))
    if len(opinions) > 0:
        opinions_all = []
        for opinion in opinions:
            single_opinion = {
                #"opinion_id": page_dom.css.select(".user-post__author-name"),
                "author": page_dom.css.select(".user-post__author-name"),
                "recommendation": page_dom.css.select(".user-post__author-recomendation"),
                "stars": page_dom.css.select(".user-post__score-count"),
                "purchased": page_dom.css.select(".review-pz"),
                #"opinion_date": page_dom.css.select(".user-post__author-name"),
                #"purchase_date": page_dom.css.select(".user-post__author-name"),
                #"useful_count": page_dom.css.select(".user-post__author-name"),
                #"unuseful_count": page_dom.css.select(".user-post__author-name"),
                #"content": page_dom.css.select(".user-post__author-name"),
                #"pros": page_dom.css.select(".user-post__author-name"),
                #"cons": page_dom.css.select(".user-post__author-name")
            }
        print(single_opinion["author"])
    else:
        print("Nie ma opinii")