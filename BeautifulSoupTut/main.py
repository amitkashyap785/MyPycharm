# If you want to scrap a website:
# 1. use the API
# 2. HTML Web Scraping using some tool like bs4

# step 0:----Install all the requirement
# pip install requests
# pip install bs4
# pip install html5lib



import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# step 1:-- Get the HTML

r = requests.get(url)
htmlContent = r.content

#print(htmlContent)

# step 2:--- Parse the HTML

soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

# Step 3  : -- HTML Tree traversal
#Commonly used types of objects:

# Get the title of the Html page
title = soup.title


# 1. - Tag
#print(type(title))
# 2. - NavigableString
#print(type(title.string))
# 3. - BeautifulSoup
#print(type(soup))

# 4. - Comment
markup = "<p><!--- this is a comment ---></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)

print(type(soup2.p.string))





# Get all the paragraphs from the page

paras = soup.find_all('p')
#print(paras)

# Get all the anchor tag from the page

anchors = soup.find_all('a')
all_links = set()
#print(anchors)

# Get all the link on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(link.get('href'))

# to get only frist paragraph
#print(soup.find('p'))

# to find class of frist paragraph

#print(soup.find('p')['class'])

# find all the elements with class lead

#print(soup.find_all('p', class_="text"))

# Get the text from the tags/soup

#print(soup.find('p').get_text())
#print(soup.get_text())





