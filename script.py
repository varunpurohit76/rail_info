#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests, collections, json, sys, argparse

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
    if table == None:
        p_content = soup.find('p')
        if 'Unavailable' in str(p_content):
            print ('Information Unavailble. Please check the train number.')
        elif 'busy' in str(p_content):
            p_content = p_content.text.strip()
            print (p_content)
        else:
            p_content = p_content.text.strip()
            print ('Train not running!')
            print (p_content)
        sys.exit()

def main():
    days = {'today' :	0,'tomorrow' : 1, 'yesterday' : -1}
    parser = argparse.ArgumentParser()
    parser.add_argument('train_num', help='Enter the train number', type = int)
    parser.add_argument('--day',help='Enter the day',choices = ['today','tomorrow','yesterday'],default='today')
    args = parser.parse_args()
    train_num = args.train_num
    day = args.day
    payload = {'tno':train_num, 'date': days[day]}
    r = ''
    try:
        r = requests.get('http://spoturtrain.com/status.php', params = payload)
    except:
        print('Unable to retrieve info, check your internet connection')
        sys.exit()
    train_info = collections.OrderedDict()
    train_info['url'] = r.url
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    is_data_available(soup)
    train_info['status'] = status(soup)
    train_info['timetable'] = timetable(soup)
    train_info = json.dumps(train_info , indent = 3)
    print (train_info)

if __name__ == "__main__": main()
