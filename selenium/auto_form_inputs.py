from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
import time

#chrome_browser = webdriver.Chrome("/Users/bleeet/Desktop/python/chromedriver")
chrome_browser = webdriver.Firefox()

#chrome_browser.maximize_window()
chrome_browser.set_window_size(900, 700)
#https://www.seleniumeasy.com/test/basic-first-form-demo.html
chrome_browser.get('http://www.seleniumeasy.com/test/basic-first-form-demo.html')
#chrome_browser.get('https://www.seleniumeasy.com/test/')

#print("Selenium Easy Demo" in chrome_browser.title)

while True:
    #lightboxClose = chrome_browser.find_element_by_class_name('at4-close')
    time.sleep(3)
    lightboxClose = chrome_browser.find_element(By.LINK_TEXT, "No, thanks!")

    if (presence_of_element_located(lightboxClose)):
        webdriver.ActionChains(chrome_browser).click_and_hold(lightboxClose).perform()
        webdriver.ActionChains(chrome_browser).release().perform()

    button = chrome_browser.find_element_by_class_name('btn-default')

    #using page.source here to check the entire page in html fomart if 'show message' exists
    #assert 'show message' in chrome_browser.page_source

    usermessage = chrome_browser.find_element_by_id('user-message')
    usermessage.clear()
    usermessage.send_keys(" i am extra cool ")
    break
