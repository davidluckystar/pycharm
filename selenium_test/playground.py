__author__ = 'amatveev'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *

def go():
    print('starting..')
    my_proxy = "proxy:3128"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://%s' % my_proxy)
    driver = webdriver.Chrome('C:\Python34\chrome_driver\chromedriver.exe',chrome_options=chrome_options)
    # open tree-project site
    driver.get('http://5.45.123.141:8080/index.xhtml')
    print('title: ' + driver.title)
    # try to login
    registration_form = driver.find_element_by_class_name('registration-form')
    username_input = registration_form.find_element_by_css_selector('div.form-group > input#user_name')
    username_input.send_keys('david.lucky.star@gmail.com')
    password_input = registration_form.find_element_by_css_selector('div.form-group > input#password')
    password_input.send_keys('123456')
    submit_btn = registration_form.find_element_by_css_selector('input[type=submit]')
    submit_btn.send_keys(Keys.ENTER)


if __name__ == "__main__":
    go()

