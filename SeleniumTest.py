# Selenium Data.world scraping

#import libraries
import time
import pandas as pd
import selenium
from selenium import webdriver

#logging in to data.world
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://data.world/login')
username = driver.find_element_by_xpath("//input[@placeholder='Username or email address']")
password = driver.find_element_by_xpath("//input[@placeholder='Password']")

#input username and password
username.send_keys("j.dejesus22@gmail.com")
password.send_keys("password")
driver.find_element_by_xpath("//button[@type='submit']").click()

#go to url
time.sleep(5)
url='https://data.world/makeovermonday/what-is-the-uks-favorite-chocolate-bar/discuss/2018-w13-what-is-the-uks-favorite-chocolate-bar/95666'
driver.get(url)

#get post
posts=driver.find_elements_by_xpath("//div[@class='post__thumbnail___33jZY DatasetCard__thumbnail___33EHZ']")
info=[]
for i in range(len(posts)):
    name = posts[i].find_element_by_xpath(".//a[@class='post__username___YIalv']")
    name=name.text
    try:
        vizpic=posts[i].find_element_by_xpath(".//img")
        vizpic=vizpic.get_attribute('src')
    except:
        vizpic=None
    try:
        link=posts[i].find_element_by_link_text('Interactive Viz').get_attribute('href')
    except:
        link=None
    info.append((name, vizpic,link))

data=pd.DataFrame(info,columns=['Name','VizPic', 'Link'])
data.to_csv('datadotworld_wk13_vizzes.csv',index=False)

'''
#get names
name_elements=driver.find_elements_by_xpath("//a[@class='post__username___YIalv']")
names=[name.text for name in name_elements[1:]]

#get viz picks
vizpic_elements=driver.find_elements_by_xpath("//img")
vizpics=[vizpic.get_attribute('src') for vizpic in vizpic_elements[11:]]

# get links
link_elements=driver.find_elements_by_link_text('Interactive Viz')
links=[link.get_attribute('href') for link in link_elements]

'''

#signout and close the window
time.sleep(3)
driver.find_element_by_xpath("//li[@class='Header__menu_account___3jT6C dw-UserSettingsDropdown dropdown']").click()
time.sleep(5)
driver.find_element_by_xpath("//li[@class='Header__itemSignOut___UfV3_']").click()
time.sleep(5)
driver.quit()
