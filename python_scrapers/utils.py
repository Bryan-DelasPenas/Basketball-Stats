from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import unicodedata, unidecode


'''
This code was based on basketball_reference scraper, removes accents from names 
'''
def remove_accents(name,team, season):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY ')
    
    if len(set(name).difference(alphabet))==0:
        return name
    
    r = get(f'https://www.basketball-reference.com/teams/{team}/{season}.html')
    team_df = None
    best_match = name
    
    # Check if the stats code was successful
    if r.status_code==200:
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        team_df = pd.read_html(str(table))[0]
        max_matches = 0
    
        for p in team_df['Player']:
            matches = sum(l1 == l2 for l1, l2 in zip(p, name))
    
            if matches>max_matches:
                max_matches = matches
                best_match = p
    
    return best_match