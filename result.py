#! python2
# python script which scrapes any student's NITT result from http://misnew.nitt.edu/NITTSTUDENT/

import os
import sys
import requests
import time
import getpass
import matplotlib.pyplot as plt
import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.firefox.options import Options

# Importing local .py files
import config # File which contains path_to_executable_file_geckodriver

browser_options = Options()
browser_options.headless = True
browser = webdriver.Firefox(executable_path=config.geckodriver_path,options=browser_options)


# predefined variables
login = False

# url's of pages
login_url    = 'http://misnew.nitt.edu/NITTSTUDENT/'
services_url = login_url+'servicesReqPage'

# Id's of elements
# elements in url : http://misnew.nitt.edu/NITTSTUDENT/
usernameElementId = 'userId'
passwordElementId = 'password'
loginBtnId        = 'loginSubmit'
loginFormId       = 'userLogin'
logoutLinkXPath       = '/html/body/div/div/div/div[3]/div[4]/span[2]/a'

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

while(not login):
    try :
        browser.get(login_url)

        # Getting user_credentials
        print('Enter your misnew credentials : ')
        time.sleep(1)
        username = input('Roll number : ')
        password = getpass.getpass('Password    : ')

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

    try:
        time.sleep(1)
        # Finding logout link element to check whether the credentials are correct
        logoutLink = browser.find_element_by_xpath(logoutLinkXPath)
        login = True # making login=true, if the credentials are correct
    except Exception as err: 
        print('Roll number or password is incorrect. Please try again.')
        time.sleep(1)
        print('')
        login = False # making login=false, since the credentials are incorrect

try:
    time.sleep(2)
    print('Successfully logged into '+browser.current_url)
    browser.get(services_url)
    print('Navigating to url : '+browser.current_url)
    time.sleep(2)

except Exception as err: 
    print(err)
    print('Probably, the site is down due to heavy traffic. Please try again after some time.')
    browser.quit()

try:
    browser.find_element_by_id(resultsNavLink).click()
    print('Retrieving results ....')
    time.sleep(1)

    selectElement = Select(browser.find_element_by_id(selectElementId))
    resultButton = browser.find_element_by_xpath(resultBtnXPath)
    print('--------------------------------')
    print('     Roll Number : '+str(username))
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
            print('     Sem '+str(len(gpa))+' GPA   : '+str(gpa[((len(gpa))-1)]))

            # Scraping value of CGPA in that sem from the cgpa input_element
            cgpaElement = browser.find_element_by_id(cgpaElementId)
            cgpa        = cgpaElement.get_attribute('value')
            selectIndex += 1
            
        else:
            exists = 0
 
    print('     CGPA        : '+ cgpa)
    print('--------------------------------')
    time.sleep(2)

    print('Plotting GPA graph ....')
    time.sleep(1)

    print(gpa[1])

    print('Graph plotted, opening graph ...')
    plt.show()
    print('Closing graph ...')

except Exception as err: 
    print(err)
    browser.quit()

browser.quit()