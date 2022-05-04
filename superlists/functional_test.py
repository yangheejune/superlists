from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'yanghj' in browser.title

