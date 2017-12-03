# ams2 staff webscrapping

import requests
r=requests.get('https://www.newvisions.org/ams2/pages/our-staff2')

#import webpage into BeautifulSoup
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text, 'html.parser')

#Create set based on HTML tags with desired data
results=soup.find_all('div', attrs={'class':'matrix-content'})
len(results)
results=results[27:]
len(results)

#name
test_result=results[0]
test_result.find('h5')
test_result.find('h5').text

#position(s)
test_result.find('p').text.strip('\n\t')

#email

test_result.find('em').get_text()

#data extraction
info=[]
for result in results:
    name=result.find('h5').text
    position=result.find('p').text.strip('\n\t')
    try: 
        email=result.find('em').get_text()
    except:
        email='NaN'
    info.append((name,position,email))
    
#convert to dataframe and export to csv
import pandas as pd
df=pd.DataFrame(info, columns=['Name','Position(s)','Email'])
    
#determining duplicates 
for column in df.columns:
   print(df.duplicated([column]))
   print(df.duplicated([column]).sum())

#Eliminating Duplicates
df.drop_duplicates(['Name'],keep='first', inplace=True)

df.to_csv('AmsTwoStaffInfo.csv', index=False)