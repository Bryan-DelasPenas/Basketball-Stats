from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import unicodedata, unidecode
import unicodedata
import re 

'''
Removes accents from string
'''
def strip_accents(text):

    # Speical case as ß is not a letter in english
    if('Tibor Plei' in text):
        text = 'Tibor Pleiss'
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
Removes accent from characters and changes it to proper letter
'''
def translate(name):
    
    special_char = ('Ã³', 'Ã–', 'ÅŸ', 'Ä±', 'Ãº', 'Ã§', 'Å¡', 'Å†', 'Å¡', 'Ä‡', 'Ä', 'Å¾', 'Ã¡', 'Å½','ÄŒ', 'Ä','Ã©', 'Ã', 'A°', 'Aª', 'a°', 'A¼', 'A¨', 'A²', 'È™',
                    'A¶', 'Å«', 'A¤', 'a£', 'AŸ', 'A«', 'A½', 'Å„', 'aŸ', 'A“', 'A£', 'a“')
    
    # 
    if any(x in name for x in special_char):
        if('Biedrin' in name):
            name = name.replace('Å¡', 'n')

        # Case for: Vlatko Cancar
        elif('Vlatko' in name):
            name = "Vlatko Cancar"

        elif('Porzi' in name):
            name = 'Kristaps Porzingis'
        
        #Case for: Guillermo diaz
        elif('Guillermo' in name):
            name = "Guillermo Diaz"

        elif('Faverani' in name):
            name = "Vitor Luiz Faverani"

        elif('Cristiano' in name):
            name = 'Cristiano Felicio'

        elif('Francisco Garc' in name):
            name = 'Francisco Garcia'

        elif('Jasikevi' in name):
            name = 'Sarunas Jasikevicius'

        elif('Kuko' in name):
            name = 'Toni Kukoc'

        elif('iulionis' in name):
            name = 'Sarunas Marciulionis'

        elif('siks' in name):
            name = 'Anzejs Pasecsiks'

        elif('undov' in name):
            name = 'Bruno Sundov'

        elif('aric' in name):
            name = "Dario Saric"

        elif('amanic' in name):
            name = 'Luka Samanic'

        elif('Jonas Valan' in name):
            name = 'Jonas Valanciunas'

        elif('George Z' in name):
            name = 'George Zidek'

        else:
            name = name.replace('Ã³', 'o')
            name = name.replace('Ã–', 'O')
            name = name.replace('ÅŸ', 's')
            name = name.replace('Ä±', 'i')
            name = name.replace('Ãº', 'u')
            name = name.replace('Ã§', 'c')
            name = name.replace('Å†', 's')
            name = name.replace('Å¡', 's')
            name = name.replace('Ä‡', 'c')
            name = name.replace('Ä', 'a')
            name = name.replace('Ã¡', 'a')
            name = name.replace('Å¾', 'z')
            name = name.replace('Å½', 'Z')
            name = name.replace('aŒ', 'C')
            name = name.replace('Ã©', 'e')
            name = name.replace('Ã', 'A')
            name = name.replace('A°', 'o')
            name = name.replace('Aª', 'e')
            name = name.replace('a°', 'I')
            name = name.replace('A¼', 'u')
            name = name.replace('A¨', 'e')
            name = name.replace('È™', 's')
            name = name.replace('A²', 'o')
            name = name.replace('A¶', 'o')
            name = name.replace('Å«', 'u')
            name = name.replace('A¤', 'a')
            name = name.replace('a£', 'g')
            name = name.replace('AŸ', 'ss')
            name = name.replace('A«', 'e')
            name = name.replace('A½', 'y')
            name = name.replace('Å„', 'n' )
            name = name.replace('aŸ', 'g')
            name = name.replace('A“', 'O')
            name = name.replace('A£', 'a')
            name = name.replace('a“', 'e')
    
    return name

