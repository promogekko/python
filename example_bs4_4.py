from bs4 import BeautifulSoup
import requests
# url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

#url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"
#response = requests.get(url)
#soup = BeautifulSoup(response.content,"html.parser")
#print(soup_page)



with open("metro.html", encoding='utf-8') as infile:
    soup = BeautifulSoup(infile, "html.parser")

#tag_th = soup.find_all('th')
#search_tr = soup.find_all('tr')
#print(search_tr)
#rows=soup.find_all(attrs={"scope": "row"})
#for tr in rows:
#    atag=tr.findChildren(text=True)
#    #print(atag)
strkey=soup.find_all("tr")
for st in strkey:
    #print(st)
    tag=st.findChildren(text=True)
    #print(tag)
    if "Wagram" in tag[1]:
        print(tag[1],tag[6])
        break
    elif tag[6] == '\n':
        print(tag[1],tag[7])
    else:
        print(tag[1],tag[6])



#print(rows)
exit()

data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
#print(data)


i=1
myarrayrow=[]
for (sta,line) in zip(tag_th,data):
    st = sta.a
    if st is not None:
        station = st.string
    if st:
        if len(line) >  2 :
            station = st.string
            myarrayrow.append((i,station,line[2][0]))
            i +=  1
print(myarrayrow)
