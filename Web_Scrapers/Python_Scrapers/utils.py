from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import unicodedata, unidecode
import unicodedata
import re 
from datetime import datetime

'''
Removes accents from string
'''
def strip_accents(text):

    # Speical case as ß is not a letter in english
    if('Tibor Plei' in text):
        text = 'Tibor Pleiss'
        return text
    elif('Gu' in text and 'mundsson' in text):
        text = 'Petur Gudmundsson'
    
    elif('Aleksandar' in text and 'or' in text):
        text = 'Aleksandar Djordjevic'

    elif("mer " in text and 'k' in text and 'A' in text):
        text = 'Omer Asik'
        return text
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

'''
Helper Function that changes season_start-season_end to season_end
'''
def remove_char(string, postion):
    # Characters before the i-th indexed 
    # is stored in a variable a 
    a = string[ : postion]  
      
    # Characters after the nth indexed 
    # is stored in a variable b 
    b = string[postion + 1: ] 
      
    # Returning string after removing 
    # nth indexed character. 
    return a + b 

def proper_dates(date):
    # Removes the comma 
    date = date.replace(',','')
    
    # Changes into YYYY-MM-DD
    datetime_object = datetime.strptime(date, "%B %d %Y").strftime('%Y-%m-%d')
    return str(datetime_object)
