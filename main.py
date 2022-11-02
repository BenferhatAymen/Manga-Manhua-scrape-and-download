from scraper import *
import os
Manhua = input('Atcho Manhua : ')
Results = search(Manhua)
names = Results[0]
links = Results[1]

s=""
for i in range(len(names)) :
    s+=f"{i+1} - {names[i]}\n"
print(s)
num = int(input("What manhua do you want to download : "))-1

link = links[num]
chapter = len(chapters(link))
dow = chapters(link)
osm = namis(link)
with open('text.txt','w+',encoding='utf-8') as f:
    osm.reverse()
    for i in range(len(osm)) :
        f.write(f"{i} - {osm[i]}\n")


froms = int(input('Beginning : '))
ends = int(input('End : '))
path = os.path.abspath(os.getcwd())
namepath = names[num]

try : 
        os.makedirs(namepath)
        paths = os.path.abspath(os.getcwd())+f"\{namepath}"
        print(paths)
except : 
       
        paths = os.path.abspath(os.getcwd())+f"\{namepath}"

for i in range(froms-1,ends):
    asm = namis(link)
    asm.reverse()
    print(asm)
    
    patha = paths+f"\{asm[i]}"
    os.makedirs(patha)
    print(patha)

    downloads(getimages(dow[i]),patha)

os.remove('text.txt')
