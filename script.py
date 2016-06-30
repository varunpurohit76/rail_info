#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import collections
import json
import sys

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

def is_data_available(soup):
    table = soup.find(id = 'eta')
    if table is None:
        p_content = soup.find('p')
        if 'Unavailable' in str(p_content):
            print ('Information Unavailble. Please check the train number.')
        else:
            p_content = p_content.text.strip()
            print ('Train not running!')
            print (p_content)
        sys.exit()

def main():
    train_num = sys.argv[1]
    payload = {'tno':train_num, 'date':'0'}
#12483
    r = requests.get('http://spoturtrain.com/status.php', params = payload)
    train_info = collections.OrderedDict()
    train_info['url'] = r.url
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    is_data_available(soup)
    train_info['status'] = status(soup)
    train_info['timetable'] = timetable(soup)
    train_info = json.dumps(train_info)
    print (train_info)

if __name__ == "__main__": main()
