import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time
import json
import atexit

from dotenv import load_dotenv
load_dotenv()

with open('Identifiers.json','r') as File:
    Store = json.load(File)

{
1   :   "Unit 1 - Information Technology Systems",
2   :   "Unit 2 - Creating Systems to Manage Information",
3   :   "Unit 3 - Using Social Media in Business",
4   :   "Unit 4 - Programming",
6   :   "Unit 6 - Website Development",
8   :   "Unit 8 - Computer Games Development",
11  :   "Unit 11 Cybersecurity & Incident Management",
}

options = webdriver.ChromeOptions()
for x in (
    "--no-sandbox",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-dev-shm-usage",
    "--window-size=1920,1200",
    "--ignore-certificate-errors"
        ):
    options.add_argument(x)
# options.headless=True
browser = webdriver.Chrome(options=options)

#ToDo - Add dynamic wait times in between settings, perhaps a while loop
def Setup():
    browser.get(Store["URL"])

    Wait = WebDriverWait(browser,60)

    Target = Wait.until(EC.element_to_be_clickable((By.NAME, 'loginfmt')))
    Target.send_keys(os.getenv('MEMAIL'),Keys.RETURN)

    Target = Wait.until(EC.element_to_be_clickable((By.NAME, 'passwd')))
    Target.send_keys(os.getenv('MPASS'),Keys.RETURN)

    Target = Wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
    Target.click()

    XPath = Store['UnitXP'].format({1:2,2:3,3:4,4:5,6:6}[2])
    Target = Wait.until(EC.element_to_be_clickable((By.XPATH,XPath)))
    Target.click()

    Wait.until(EC.element_to_be_clickable((By.XPATH,Store['JoinXP'])))
    try:
        Target = browser.find_element_by_xpath(Store['JoinXP'])
        Target.click()
    except selenium.common.exceptions.TimeoutException:
        print('No Valid Meeting')

@atexit.register
def ExitHandler():
    input('Press Enter To Close Browser')
    browser.close()

if __name__ == "__main__":
    Setup()