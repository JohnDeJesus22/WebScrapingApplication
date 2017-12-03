# Bronx School Staff Webscrapping

import requests
p=requests.get('https://www.newvisions.org/ams2/pages/our-staff2')

#Import webpage into BeautifulSoup and parsing it
from bs4 import BeautifulSoup
soup=BeautifulSoup(p.text, 'html.parser')

#Create set based on HTML tags with desired data
results=soup.find_all('div', attrs={'class':'matrix-content'})
len(results)
results=results[27:]
len(results)

#Testing with the first teacher and obtaining the name
test_result=results[0]
test_result.find('h5')
test_result.find('h5').text

#Obtaining position(s)
test_result.find('p').text.strip('\n\t')

#Obtaining email
test_result.find('em').get_text()

#Data extraction
info=[]
for result in results:
    name=result.find('h5').text
    position=result.find('p').text.strip('\n\t')
    try: 
        email=result.find('em').get_text()
    except:
        email='NaN'
    info.append((name,position,email))
    
#Convert to dataframe and export to csv
import pandas as pd
df=pd.DataFrame(info, columns=['Name','Position(s)','Email'])
    
#Determining duplicates 
for column in df.columns:
   print(df.duplicated([column]))
   print(df.duplicated([column]).sum())

#Eliminating duplicates
df.drop_duplicates(['Name'],keep='first', inplace=True)

#Export to csv without numbered indices
df.to_csv('BronxSchoolStaffInfo.csv', index=False)