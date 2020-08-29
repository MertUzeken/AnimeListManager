# Author: Mert Uzeken
# Project Name: Anime List Manager

import os, _osx_support, sys, openpyxl, urllib, requests, shutil
import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request  # Python 3
sys.path.append('../')

class Fetching:
    def __init__(self):
       self.Search_Query()
       self.get_Page()
       self.title_Crawler()
       self.icon_Crawler()

    def get_Page(self):
        import requests
        reg_url = "https://randaris.app/members/detail/26809/KiriSenpai"
        headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Referer': 'https://cssspritegenerator.com',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        self.MyClient = requests.get(reg_url, headers=headers, timeout=5)
        self.html_stream = self.MyClient.text

    def title_Crawler(self):
        page_soup = soup(self.html_stream, "html.parser")
        elements = page_soup.findAll('tbody')
        count = 0                                                               #Count the tbody index to find first and last tbody. (Completed[1] , Planned[2])
        for element in elements:                                                #ToDo: Delete for loop instead get list index count. Get rid of count.
            count += 1
        count -= 1
        title_completed = []
        title_planned = []

        for element_completed in elements[0]:
            try:
                title_completed.append((element_completed.a.string))
            except AttributeError:
                pass

        for element_planned in elements[count]:
            try:
                title_planned.append((element_planned.a.string))
            except AttributeError:
                pass

        #Write to xlsx file (excel)
        completed = pd.DataFrame({'Completed': title_completed})
        completed.to_excel('completed.xlsx', encoding='utf-8',index=False)
        planned = pd.DataFrame({'Planned': title_planned})
        planned.to_excel('planned.xlsx', encoding='utf-8',index=False)

        print(count)

    def icon_Crawler(self):
        dir = os.getcwd() + '/thumbnails'                                       # Image Folder
        if not os.path.exists(dir):                                             # Create Folder if not already existing
            os.mkdir(dir)

        whole_page = soup(self.html_stream,"html.parser")                       #Gets the whole HTML Page
        table_bodies = whole_page.findAll('tbody')                              #Finds all table bodys and inserts them into a list
        completed_half = soup(str(table_bodies[0]), "html.parser")              #Here we take only the first list which is the completed list. (parse it into the soup function as String)
        new_elements = completed_half.findAll('tr', {"data-title": True})       #Now we do another search and Find every single table row.

        clean_links = []
        counter = 0

        for element in new_elements:                                            #You get only the data-title from the bracket <tr .... data-title: www.somepicture.com/23421.jpg
            link = element['data-title']
            s = soup(link, 'html.parser')
            clean_links.append(s.find('img')['src'])                            #Right into the list

        for image in clean_links:
            r = requests.get(image, stream=True)
            if r.status_code == 200:
                counter += 1
                with open(str(dir) + '/' + str(counter) + '.jpg', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)

    def Search_Query(self):
        True
        #Search query may get obselety due to changes in the project scope

def main():
    #ToDo: Transfer main to GUI class.
    #The main function is obsolete
    new1 = Fetching()

main()
