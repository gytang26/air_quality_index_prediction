#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 17:19:03 2021

@author: ctgy
"""

from Plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016,avg_data_2017, avg_data_2018
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

def met_data(month, year):
    
    #scrapping html data with 'rb' mode
    file_html = open('Data/Html_Data/{}/{}.html'.format(year, month), 'rb')
 
    #read function after scrapping
    plain_text = file_html.read()
    
    tempD = []
    finalD = []
    
    #initialise beautiful soup
    soup = BeautifulSoup(plain_text, 'lxml')
    
    # loop with finall function inside table that contain 'medias mensuales numspan' class
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        #nexted loop for tbody in table, tbody is from f12 = inspect on website
        for tbody in table:
            #nested loop for tr in tbody, tr is text row from website
            for tr in tbody:
                #tr.get_text function, pickup text after interations
                a = tr.get_text()
                # append into tempD
                tempD.append(a)
            
            

    #because we don know it has how many features in a row. and we have 15 features, divide total length of tempD by 15
    rows = len(tempD)/15
    
    #iterate each row
    for times in range(round(rows)):
        #nested loop the 15 columns in each row
        newtempD = []
        for i in range(15):
            #get data and append value into new list (newtempD), then pop
            newtempD.append(tempD[0])
            tempD.pop(0)
            
        #append into finalD list
        finalD.append(newtempD)
        
     #drop null or useless columns, or we can say it is specific row in dataframe we created
    length = len(finalD)
     
     #pop last column or row in our dataframe named "monthly...."
     #pop first which is all the features name such as day TM....
    finalD.pop(length-1)
    finalD.pop(0)
     
     
    #loop to remove the 6th
    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)
     
    return finalD




def data_combine(year, cs):
    for a in pd.read_csv('Data/Real_Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Real_Data"):
        os.makedirs("Data/Real_Data")
        
        
    for year in range(2013,2019):
        final_data = []
        
        with open("Data/Real_data/real_" + str(year) + ".csv", "w") as csvfile:
            wr = csv.writer(csvfile, dialect = 'excel')
            wr.writerow(
                ['T', 'TM','Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp

        
        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()
        
        if len(pm) == 364:
            pm.insert(364, '-')
        
        for i in range(len(final_data)-1):
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])
            
        with open('Data/Real_Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600)
    data_2018 = data_combine(2018, 600)
     
    total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018
    
    with open('Data/Real_Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
    
  
#create df
df=pd.read_csv('Data/Real_Data/Real_Combine.csv')   
    

















