#! python2
# python script which scrapes any student's NITT result from http://misnew.nitt.edu/NITTSTUDENT/

import os
import sys
import requests
import time
import getpass
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

# url's of pages
login_url    = 'http://misnew.nitt.edu/NITTSTUDENT/'
services_url = login_url+'servicesReqPage'

# Id's of elements

# elements in url : http://misnew.nitt.edu/NITTSTUDENT/
usernameElementId = 'userId'
passwordElementId = 'password'
loginBtnId        = 'loginSubmit'
loginFormId       = 'userLogin'

# element in url : http://misnew.nitt.edu/NITTSTUDENT/servicesReqPage
resultsNavLink    = 'ExamResults'

# elements in url : http://misnew.nitt.edu/NITTSTUDENT/resultPublish
selectElementId   = 'sessionId'
resultBtnXPath  = '//*[@id="RightCommonColum"]/div/table/tbody/tr[2]/td/table/tbody/tr/td/input'
cgpaElementId     = 'cgpa'

selectIndex = 1

try :
    browser.get(login_url)

    # Getting user_credentials
    username = input('Roll number : ')
    password = getpass.getpass('Password : ')

    usernameElement = browser.find_element_by_id(usernameElementId)
    passwordElement = browser.find_element_by_id(passwordElementId)
    loginBtn        = browser.find_element_by_id(loginBtnId)
    loginForm       = browser.find_element_by_id(loginFormId)

    # Clearing default values in inputs
    usernameElement.clear()
    passwordElement.clear()

    # Entering user_credentials in form
    usernameElement.send_keys(username)
    passwordElement.send_keys(password)
    loginForm.submit()
    time.sleep(2)

except Exception as err: 
    print(err)
    browser.quit()

print 'Successfully logged into '+browser.current_url

try:
    browser.get(services_url)
    print 'Navigating to url : '+browser.current_url
    time.sleep(1)

    browser.find_element_by_id(resultsNavLink).click()
    print "Retrieving results ...."
    time.sleep(1)

    # selecting option in select
    selectElement = Select(browser.find_element_by_id(selectElementId))
    selectElement.select_by_index(selectIndex)

    # Clicking 'Show results' button to display results
    resultButton = browser.find_element_by_xpath(resultBtnXPath)
    resultButton.click()
    time.sleep(2)

    # Scraping value of CGPA from the cgpa input_element
    cgpaElement = browser.find_element_by_id(cgpaElementId)
    cgpa = cgpaElement.get_attribute('value')
    print 'CGPA : '+ cgpa

except Exception as err: 
    print(err)
    browser.quit()

browser.quit()