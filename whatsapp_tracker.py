from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
options.add_argument('lang=en')
options.add_argument('--lang=en')

browser = webdriver.Chrome(r'/usr/local/bin/chromedriver', options=options) #Put your chromedriver location here

browser.get('http://web.whatsapp.com/')


def wait_until(somepredicate, timeout, period=0.25):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if somepredicate: return True
    time.sleep(period)
  return False

def check_exists_by_class(myClass):
    try:
        browser.find_element_by_class_name(myClass)
    except NoSuchElementException:
        return False
    return True

def check_user_status():

  try:
    browser.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
    userStatus = "online"
  except:
    userStatus = "offline"

  return userStatus

try:
    myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_3l6Cf')))
except TimeoutException:
    print ("Loading Error or session already initiated")

if (browser.find_element_by_class_name('_3l6Cf')): 
  print('Please Scan the QR-Code')

while (browser.find_elements_by_class_name('_3l6Cf')):
  time.sleep(0.5)

print('Please select user manually')

while(not browser.find_elements_by_class_name('YEe1t')):
  time.sleep(0.5)

selectedUser = browser.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').get_attribute("innerHTML")

print("Selected User:   " + selectedUser)
time.sleep(2)

userStatus = check_user_status()

print(f"{selectedUser} is {userStatus}")

while True:
  if not userStatus == check_user_status():
    userStatus = check_user_status()
    print(f"{time.ctime()}: {selectedUser} is {userStatus}")
    time.sleep(5)
  else:
    time.sleep(5)
