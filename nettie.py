import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randrange

# lisättäviä asioita:
# moottorin koko span class engine size

#base_url sisältää avensiksen tietyillä spekseillä. Automerkkiä ja mallia voi vaihtaa url:ää editoimalla. 
base_url='https://www.nettiauto.com/toyota/avensis'
hinnasto = []
x=1
pagecount=5

while x <= pagecount:
    current_url= base_url + '&Page='+ str(x)
    html = requests.get(str(current_url))
    html = requests.get(base_url)
    soup = BeautifulSoup(html.text, "html.parser")
    unwanted = soup.find('div', class_="upsellAd")
    unwanted.extract()
    print(unwanted.text)
    hinnat = soup.find_all('a', class_="childVifUrl")
    for hinta in hinnat:
        hinnasto.append({
            'merkki': hinta.attrs['data-make'],
            'malli': hinta.attrs['data-model'],
            'kilometrit': hinta.attrs['data-mileage'],
            'hinta': hinta.attrs['data-price'],
            'vuosi': hinta.attrs['data-year'],
            })
    sleep(randrange(2,5))
    print(str(x) + " / " + str(pagecount) + " done")
    x+=1


toCSV = hinnasto
keys = toCSV[0].keys()
with open('nettiauto.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)



print("writing complete")
