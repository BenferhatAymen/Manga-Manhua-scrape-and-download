#importing nedded libraries
import requests
import json
from lxml import html 


#url 

url = "https://aresmanga.com"

#search for manhuas/manhwas
def search(fName):
    name = fName.replace(" ","%20")
    page = requests.get(f"{url}/?s={name}")
    tree = html.fromstring(page.text)
    namess = tree.xpath('//div[@class="tt"]/text()')
    names = [na.replace('\t','').replace("\n","") for na in namess]
    hrefs = tree.xpath('//div[@class="bsx"]/a/@href')
    return names,hrefs

#get the chapters list
def chapters(link):
    page = requests.get(link)
    tree = html.fromstring(page.text)
    #names = tree.xpath('//div[@class="eph-num"]/a/span[@class="chapternum"]/text()')[1::]



    hrefs = tree.xpath('//div[@class="eph-num"]/a/@href')[1::]

 
    return hrefs 
#names
def namis(link):
    page = requests.get(link)
    tree = html.fromstring(page.text)
    names = tree.xpath('//div[@class="eph-num"]/a/span[@class="chapternum"]/text()')[1::]



    #hrefs = tree.xpath('//div[@class="eph-num"]/a/@href')[1::]

 
    return names


# get manhua pages as a list 
def getimages(chap):
    page = requests.get(chap)
    tree = html.fromstring(page.text)
    href = tree.xpath('//div[@class="wrapper"]/script[1]/text()')[0]
    s = href.find("[")
    like_list = href[href.find("[",s+1):href.find("]")+1]
    res = json.loads(like_list)
    
    
    return res 

def downloads(listC : list,path):
    
    for i in range(len(listC)): 
        response = requests.get(listC[i])
        with open(f"{path}\{str(i+1)}.png","wb+") as f:
            f.write(response.content)



