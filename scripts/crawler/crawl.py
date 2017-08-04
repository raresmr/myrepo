import re
import mechanize
from bs4 import BeautifulSoup
import urllib
import requests

br = mechanize.Browser()
f = open('output','a')

##### robots.txt verification

urls = ['http://visual.ly/cccccc', 'http://visual.ly/what-are-odds',
'http://dev.visual.ly/cccccc', 'http://dev.visual.ly/what-are-odds',
'http://stage.visual.ly/cccccc', 'http://stage.visual.ly/what-are-odds']

f.write('###Robots.txt verification####'+'\n')
for x in urls:
 f.write('<br>')
 try:
  r = br.open(x)
  f.write('<font color="#009900">' + 'Robots are not blocked on ' + x + '</font>'  + '\n')
 except Exception,e:
  f.write('<font color="#cc0000">' + str(e) + ' ' + x + '</font>' + '\n')
f.write('<br>'+'<br>')

##### verify tags
f.write('###Tags verification####'+'\n')
for url in urls:
 f.write('<br>')
 r = requests.get(url)
 html_content = r.text
 soup = BeautifulSoup(html_content)

 tags = soup.findAll('meta', {"name":"robots"})

 if not tags:
   f.write('<font color="#009900">' + 'Can be crawled ' + url + '</font>' + '\n')
 else:
    for tag in tags:
       f.write('<font color="#cc0000">' + tag['content'] + ' ' + url + '</font>' + '\n')
