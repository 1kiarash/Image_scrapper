import requests
import bs4
import time

from bs4 import BeautifulSoup

main_page=requests.get("https://www.flickr.com/photos/charleshildreth/page4")
time.sleep(5)
soup = BeautifulSoup(main_page.content , 'html.parser')
script = soup.find_all('script')
code=[]
for i in range(0,len(script)):
    name = script[i].text
    #print(name)
    k = len(name)
    if k != 0 :
       for j in range(0 , k):
            if name[j:j+6]==',"id":':
                code.append(name[j+7:j+17])
    else:
        print("no")
        i = i+1

print(code[1])
#print (second_page.text)
base_url = 'https://www.flickr.com/photos/charleshildreth/'
URL = []
for i in range(0 , len(code)-1):
    if code[i] != code[i+1]:
        URL.append(base_url + code[i])
    else : i = i+1

for count in range (0 , len(URL)):
    print(URL[count])
    
