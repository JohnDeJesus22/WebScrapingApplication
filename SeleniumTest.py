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

username.send_keys("username")
password.send_keys("password")

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.find_element_by_xpath("//li[@class='Header__menu_account___3jT6C dw-UserSettingsDropdown dropdown']").click()
time.sleep(5)
driver.find_element_by_xpath("//li[@class='Header__itemSignOut___UfV3_']").click()
time.sleep(5)
driver.quit()

#html to get post using first example
#1. full post: span tag with id=6 digit number
#items we need:

#2. Username
#<a class="post__username___YIalv" href="/lunarmodule7">@lunarmodule7</a>

#3. Viz Pick
#<img src="//dataworld-discourseuploads-p-us-east-1.s3.amazonaws.com/original/2X/f/fb8dd0713f03d72e8906adab5a7a51ab164d1830.jpg" alt="𝗧𝗼𝗽 𝟭𝟬 𝗖𝗵𝗼𝗰𝗼𝗹𝗮𝘁𝗲 𝗕𝗮𝗿𝘀 𝗶𝗻 𝗗𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁 𝗔𝗴𝗲 𝗚𝗿𝗼𝘂𝗽 𝗶𝗻 𝗨𝗞">

#4. Viz Link (inside a tag of href)
#<a href="https://public.tableau.com/views/Top10ChocolateBars/1?:embed=y&amp;:display_count=yes&amp;publish=yes" target="_blank" rel="nofollow">Interactive Viz</a>