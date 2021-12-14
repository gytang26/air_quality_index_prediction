#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:45:45 2021

@author: ctgy
"""

import pandas as pd
import matplotlib.pyplot as plt


def avg_data_2013():
    
    temp_i = 0
    average = []
    #convert 24 row into dataframe
    #chunksize = how many records going to take = 24 records
    for rows in pd.read_csv('Data/AQI/aqi2013.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df=pd.DataFrame(data=rows)
        
        #iterrows, taking 'PM2.5' data in that 24 hours and append into list
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
     
        #iterate data list, if the type of i is float or int
        #add value ++
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
               
            #else if type is string
            # if not equal to 'NoData' , 'PwrFail', '---', 'InVld"
            #convert them to float and add temperature
            elif type(i) is str:
                if i!= 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temperature = float(i)
                    add_var = add_var + temperature
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    
    return average
    
    

def avg_data_2014():
    
    temp_i = 0
    average = []
    #chunksize = how many records going to take = 24 records
    for rows in pd.read_csv('Data/AQI/aqi2014.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df=pd.DataFrame(data=rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
                
            elif type(i) is str:
                if i!= 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temperature = float(i)
                    add_var = add_var + temperature
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    
    return average


def avg_data_2015():
    
    temp_i = 0
    average = []
    #chunksize = how many records going to take = 24 records
    for rows in pd.read_csv('Data/AQI/aqi2015.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df=pd.DataFrame(data=rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
                
            elif type(i) is str:
                if i!= 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temperature = float(i)
                    add_var = add_var + temperature
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    
    return average

def avg_data_2016():
    
    temp_i = 0
    average = []
    #chunksize = how many records going to take = 24 records
    for rows in pd.read_csv('Data/AQI/aqi2016.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df=pd.DataFrame(data=rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
                
            elif type(i) is str:
                if i!= 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temperature = float(i)
                    add_var = add_var + temperature
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    
    return average


def avg_data_2017():
    
    temp_i = 0
    average = []
    #chunksize = how many records going to take = 24 records
    for rows in pd.read_csv('Data/AQI/aqi2017.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df=pd.DataFrame(data=rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
                
            elif type(i) is str:
                if i!= 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temperature = float(i)
                    add_var = add_var + temperature
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    
    return average


def avg_data_2018():
    
    temp_i = 0
    average = []
    #chunksize = how many records going to take = 24 records
    for rows in pd.read_csv('Data/AQI/aqi2018.csv', chunksize = 24):
        add_var = 0
        avg = 0.0
        data = []
        df=pd.DataFrame(data=rows)
        
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
                
            elif type(i) is str:
                if i!= 'NoData' and i!= 'PwrFail' and i!= '---' and i!= 'InVld':
                    temperature = float(i)
                    add_var = add_var + temperature
        
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    
    return average




if __name__ == "__main__":
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()
    
    plt.plot(range(0,365), lst2013, label='2013 data')
    plt.plot(range(0,364), lst2014, label='2014 data')
    plt.plot(range(0,365), lst2015, label='2015 data')



















