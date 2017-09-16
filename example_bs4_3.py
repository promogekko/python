from bs4 import BeautifulSoup
import requests

url = r"https://en.wikipedia.org/wiki/List_of_stations_of_the_Paris_M%C3%A9tro"

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
#print(soup)

tag_th = soup.find_all("th")
rows = soup.findAll('tr')
#print(len(rows))

data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
#print(data)

i=1
myarrayrow=[]
for (station,ligne) in zip(tag_th,data):
    st = station.a
    if st:
        #print st.string
        #print len(ligne)
        if len(ligne) >2 :
            stat = st.string
            myarrayrow.append((i,stat,ligne[2][0]))
            i = i + 1
print(myarrayrow)

