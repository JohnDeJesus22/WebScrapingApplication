# Selenium Testing

import time
import selenium
from selenium import webdriver

#test code from Selenium docs
driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

#logging in to data.world with selenium success on 4/9/18 with logging in and out
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://data.world/login')
username = driver.find_element_by_xpath("//input[@placeholder='Username or email address']")
password = driver.find_element_by_xpath("//input[@placeholder='Password']")

#input username and password
username.send_keys("username")
password.send_keys("password")
driver.find_element_by_xpath("//button[@type='submit']").click()

#go to url and then signout
time.sleep(5)
url='https://data.world/makeovermonday/what-is-the-uks-favorite-chocolate-bar/discuss/2018-w13-what-is-the-uks-favorite-chocolate-bar/95666'
driver.get(url)

#get names
name_elements=driver.find_elements_by_xpath("//a[@class='post__username___YIalv']")
names=[name.text for name in name_elements[1:]]

#get viz picks
vizpic_elements=driver.find_elements_by_xpath("//img")
vizpics=[vizpic.get_attribute('src') for vizpic in vizpic_elements[11:]]#slicing here not index
#one?

#get viz links: neeed to adjust to get correct links
link_elements=driver.find_elements_by_xpath("//div[@class='Markdown__content___3thyu']//p//a")
links=[link.get_attribute('href') for link in link_elements]

time.sleep(3)
driver.find_element_by_xpath("//li[@class='Header__menu_account___3jT6C dw-UserSettingsDropdown dropdown']").click()
time.sleep(5)
driver.find_element_by_xpath("//li[@class='Header__itemSignOut___UfV3_']").click()
time.sleep(5)
driver.quit()


#html to get post using first example
#website
#https://data.world/makeovermonday/what-is-the-uks-favorite-chocolate-bar/discuss/2018-w13-what-is-the-uks-favorite-chocolate-bar/95666

#1. full post: span tag with id=6 digit number or use div class='caption'
#items we need:

#2. Username
#<a class="post__username___YIalv" href="/lunarmodule7">@lunarmodule7</a>

#3. Viz Pick
#<img src="//dataworld-discourseuploads-p-us-east-1.s3.amazonaws.com/original/2X/f/fb8dd0713f03d72e8906adab5a7a51ab164d1830.jpg" alt="𝗧𝗼𝗽 𝟭𝟬 𝗖𝗵𝗼𝗰𝗼𝗹𝗮𝘁𝗲 𝗕𝗮𝗿𝘀 𝗶𝗻 𝗗𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝗔𝗴𝗲 𝗚𝗿𝗼𝘂𝗽 𝗶𝗻 𝗨𝗞">

#4. Viz Link (inside a tag of href)
#<a href="https://public.tableau.com/views/Top10ChocolateBars/1?:embed=y&amp;:display_count=yes&amp;publish=yes" target="_blank" rel="nofollow">Interactive Viz</a>