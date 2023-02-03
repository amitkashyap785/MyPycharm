

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
URL = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
# HTTP Request
webpage = requests.get(URL, headers=HEADERS)
#print(webpage)

grab = requests.get(URL)
soup_list = BeautifulSoup(grab.text, 'html.parser')

#opening a fine in write mode
f = open("test1.txt", "w")
# traverse paragraphs from soup_list
for link in soup_list.find_all("a"):
    data = link.get('href')
    f.write(data)
    f.write("\n")
f.close()

#print(type(webpage.content))

# Soup Object containing all data

soup = BeautifulSoup(webpage.content, "html.parser")

#print(soup)


# Fetch links as List of Tag Objects
links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
#print(links)

links_list = []

#link = links[i].get('href')

# Loop for extracting links from Tag Objects
for link in links:
    links_list.append(link.get('href'))
    #print(links_list)

    d = {"product_Url": [], "title": [], "price": [], "rating": [], "reviews": []}

#product_list = "https//www.amazon.in" + link

 # Loop for extracting product details from each link

    for link in links_list:
        new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        #print(new_soup)
        #print(new_webpage)

        d['title'].append(get_title(new_soup))
        


        new_soup.find("span", attrs={"id": "productTitle"})


def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_product_Url(soup):
    try:
        # Outer Tag Object
        product_Url = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigatableString Object
        product_Url_value = product_Url.text

        # Title as a string value
        product_Url_string = product_Url_value.strip()

    except AttributeError:
        product_Url_string = ""

    return product_Url_string

def get_result_url(soup):



# save data into an output
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)

    amazon_df


