#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:46:20 2021

@author: ctgy
"""

import os
import time
import requests
import sys 


#from 2013 to 2018, location = delhi
def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month < 10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(
                                                                            month,
                                                                            year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(
                                                                            month,
                                                                            year)
           
            texts = requests.get(url, verify = False)
            text_utf = texts.text.encode('utf-8')
            
            #ceate folder inside HTml data based on every year
            #make sure path format is correct
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
                
            #use open function open each year and month and insert the whole text from text_utf
            # .html file is because we are creating or retrieving html file
            with open("Data/Html_Data/{}/{}.html".format(year, month), "wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
        
if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("Time taken {}".format(stop_time - start_time))