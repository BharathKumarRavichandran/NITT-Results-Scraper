#! python3
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

# Importing local .py files
import config # File which contains path_to_executable_file_geckodriver

browser = webdriver.Firefox(executable_path=config.geckodriver_path)

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
selectElementId = 'sessionId'
resultBtnXPath  = '//*[@id="RightCommonColum"]/div/table/tbody/tr[2]/td/table/tbody/tr/td/input'
gpaElementId    = 'gpa'
cgpaElementId   = 'cgpa'

selectIndex = 1
gpa         = list()
cgpa        = 'NA'

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
    print 'Retrieving results ....'
    time.sleep(1)

    selectElement = Select(browser.find_element_by_id(selectElementId))
    resultButton = browser.find_element_by_xpath(resultBtnXPath)
    print('Roll Number : '+str(username))
    exists = 1

    while((exists) and (selectIndex <= 12)):
        # selecting option in select
        selectElement.select_by_index(selectIndex)

        # Clicking 'Show results' button to display results
        resultButton.click()
        time.sleep(3)

        if(len(browser.find_elements_by_id(gpaElementId))>0):

            gpaElement = browser.find_element_by_id(gpaElementId)
            gpa.append(float(gpaElement.get_attribute('value')))
            print 'Sem '+str(len(gpa))+' GPA : '+str(gpa[((len(gpa))-1)])

            # Scraping value of CGPA in that sem from the cgpa input_element
            cgpaElement = browser.find_element_by_id(cgpaElementId)
            cgpa        = cgpaElement.get_attribute('value')
            selectIndex += 1
            
        else:
            exists = 0
 
    print 'CGPA : '+ cgpa

except Exception as err: 
    print(err)
    browser.quit()

browser.quit()