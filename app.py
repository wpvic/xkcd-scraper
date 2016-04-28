#!/usr/bin/python
#Dls all xkcd comics
import os
import bs4
import requests

url='http://xkcd.com'

if(not os.path.exists('./xkcd')):
    print('Creating directory ./xkcd...')
    os.makedirs('xkcd')
    if(os.path.exists('./xkcd')):
        print('Directory created sucessfully!')
os.chdir('xkcd')

while not url.endswith('#'):
    print('Downloading from %s' %url)
    currentPage = requests.get(url)
    currentPage.raise_for_status()

    currentPageSoup = bs4.BeautifulSoup(currentPage.text)

    image=currentPageSoup.select('#comic img')
    if image == []:
        print('Couldn\'t find comic image')
    else:
        comicUrl = 'http:'+image[0].get('src')
        print('Downloading Image %s...' %(comicUrl))
        res=requests.get(comicUrl)
        res.raise_for_status



    image_file=open(os.path.basename(comicUrl),'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()


    prevLink = currentPageSoup.select('a[rel="prev"]')[0]
    url='http://xkcd.com/'+prevLink.get('href')

print('Finished downloading all comics.')