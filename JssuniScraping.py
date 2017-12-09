# Scraping of Website for Bhargava Reddy Morampalli

#import webpage with requests
import requests
p=requests.get('https://jssuni.edu.in/JSSWeb/WebShowFromDB.aspx?MODE=SSMD&PID=10002&CID=3&DID=2&MID=0&SMID=10402')

#import page into BeautifulSoup and parse it
from bs4 import BeautifulSoup
soup=BeautifulSoup(p.text, 'html.parser')

#Create Set with HTML tags based on results
results=soup.find_all('div', attrs={'class':'col-sm-9'})
len(results)
results=results[1:]
len(results)

#Testing for loop

#Name
test_result=results[0]
test_result.find('h2').text

#Designation
test_result.find('p').contents[1].strip(' ')

#Email
test_result.find('p').contents[4].strip(' ')

#Qualifications
test_result.find('p').contents[7].strip(' ')

#No. of Publications
test_result.find('p').contents[10].strip(' ')

#data extraction, try/except for entry index 8
info=[]
for result in results:
    name=result.find('h2').text
    designation=result.find('p').contents[1].strip(' ')
    email=result.find('p').contents[4].strip(' ')
    qualifications=result.find('p').contents[7].strip(' ')
    try:
        publications=result.find('p').contents[10].strip(' ')
    except:
        publications='NaN'
    info.append((name,designation,email,qualifications,publications))

#Import Pandas and Convert to Data Frame
import pandas as pd
df=pd.DataFrame(info,columns=['Name','Designation', 'Email','Qualifications', 'TotalPublications'])

#Export to csv without indices
df.to_csv('JssunPharmaceuticsDepartmentInfo.csv', index=False)
    
