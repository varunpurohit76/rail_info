#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import collections
import json

def timetable(soup):
    table =  soup.find(id='eta')
    rows = table.find_all('tr')
    data = collections.OrderedDict()
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        cols = [ele.split('\n')[0] for ele in cols]
        data[cols[0]] = cols[1]
    return data

def status(soup):
    all_tables = soup.find_all('table')
    status_table = all_tables[1]
    content = status_table.find_all('td')
    content = [" ".join(ele.text.split()) for ele in content]
    return content

def main():
    payload = {'tno':'12952', 'date':'0'}
    r = requests.get('http://spoturtrain.com/status.php', params = payload)
    train_info = collections.OrderedDict()
    train_info['url'] = r.url
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    train_info['status'] = status(soup)
    train_info['timetable'] = timetable(soup)
    train_info = json.dumps(train_info)
    print (train_info)

if __name__ == "__main__": main()
