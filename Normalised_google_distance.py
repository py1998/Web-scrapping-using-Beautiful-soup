# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:57:15 2019

@author: Porush
"""
import requests
import math
import csv
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import time

def about_result(search):
    #google search will start by request.get
    r = requests.get("https://www.google.com/search", params={'q':search})
    soup = BeautifulSoup(r.text, "lxml")
    res = soup.find("div", {"id": "resultStats"})
    #finding number of hits using beautiful soup
    t = int(res.text.replace(",", "").split()[1])
    return t

the = about_result("the")
NGD_list = []
Human_mean = []
cnt = 0
#opening combined.csv file
with open(r'wordsim353/combined.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:    
        #to skip first row
        if cnt!=0:
            #storing mean data in list human_mean
            #I have reversed mean values because originally higher mean means
            #lower ngd so now they both will go in same way
            Human_mean.append((10 - float(row[2]) )/10)
            first_word = about_result(row[0])
            second_word = about_result(row[1])
            combined = about_result(row[0] + " " + row[1])
            #finding NGD value between 2 words in a row from file combined.csv
            num = math.log(first_word,2) - math.log(combined,2)
            den = math.log(the,2) - math.log(second_word, 2) 
            ngd = num/den
            #converting ngd value to its Tan inverse to reduce the data set limits
            NGD_list.append((math.atan(float(ngd))))
            time.sleep(5)
        cnt = cnt + 1
        print(cnt)

#plotting the graph
plt.plot(Human_mean, NGD_list, 'ro')
plt.xlabel('NGD value between two words')
plt.ylabel('mean value between two words')
plt.title('NGD vs Mean values')
plt.show()




        