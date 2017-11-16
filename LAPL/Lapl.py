import pandas as pd
from time import sleep
from random import randint

dfs = []

# PAGES 0 - 3 SCRAPE
url = 'http://www.lapl.org/whats-on/calendar?page={}'

#Let the process sleep after some seconds so that your IP does not get banned while scraping large data
sleep(randint(8, 15))

for i in range(4):
    dframe = pd.read_html(url.format(i), header=None)[0]\
                         .rename(columns={0:'Timings', 1:'Description', 2:'Location',
                                          3:'People', 4:'Category'})
    dfs.append(dframe)

finaldf = pd.concat(dfs)
finaldf.to_csv('Output.csv')