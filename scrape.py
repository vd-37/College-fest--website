import requests
from bs4 import BeautifulSoup
from requests.api import request
response = requests.get("https://webgeeks-2.herokuapp.com/sonnet1.html")
soup = BeautifulSoup( response.content , 'html.parser')
classes = [value 
           for element in soup.find_all(class_=True) 
           for value in element["class"]]
print(list(set(classes)))      
