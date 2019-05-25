# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:18:40 2019

@author: Porush
"""
import requests
import math
from bs4 import BeautifulSoup

def about_result(search):
    #google search will start by request.get
    r = requests.get("https://www.google.com/search", params={'q':search})
    soup = BeautifulSoup(r.text, "lxml")
    res = soup.find("div", {"id": "resultStats"})
    #finding number of hits using beautiful soup
    t = int(res.text.replace(",", "").split()[1])
    return t
#take input a space seperated string of 2 words
word = raw_input().split(' ')
#Number of hits for the words
first_word = about_result(word[0])
second_word = about_result(word[1])
combined = about_result(word[0] + " " + word[1])
the = about_result("the")

#aapplying ngd formula
num = math.log(first_word,10) - math.log(combined,10)
den = math.log(the,10) - math.log(second_word, 10)
ngd = num/den
print(ngd)

