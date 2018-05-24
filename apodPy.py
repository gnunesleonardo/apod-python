## Created by Leonardo G. Nunes
## http://github.com/gnunesleonardo/

import urllib.request
import datetime
import sys

def find(html, start, end):
    i, ret = 0, ''
    find = html.find(start)
    while (html[find+len(start)+i] != end):
        ret = ret+html[find+len(start)+i]
        i = i+1
    return ret

with open('apodInfo.txt') as apodInfo:
    infos = apodInfo.readlines()

for line in infos:
    print(line, end='')

print('\nChoose an option\n0 - Enter Date\n1 - Today')
option = int(input())

if option is 0:
    print('\nEnter Date (month-day-year)\nExample: 07-05-1996')
    month, day, year = sys.stdin.readline().strip().split('-')
    date = datetime.datetime(int(year), int(month), int(day)).strftime('%y%m%d')
    pageurl = 'https://apod.nasa.gov/apod/ap'+date+'.html'
    dispDate = datetime.datetime(int(year), int(month), int(day)).strftime('%B %d, %Y')
else:
    pageurl = 'https://apod.nasa.gov/'
    dispDate = datetime.datetime.now().strftime('%B %d, %Y')

apod = urllib.request.urlopen(pageurl)
html = apod.read().decode('utf8')

imgurl = 'https://apod.nasa.gov/apod/'+find(html, '<IMG SRC="', '"')
title = find(html, '<b>', '<')

print('\n>>>'+title)
print('>>> '+dispDate)
print('>>> Page URL\n'+pageurl)
print('>>> Image URL\n'+imgurl)
