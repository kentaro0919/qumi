from selenium import webdriver
from pyvirtualdisplay import Display
from selenium import webdriver
import unittest
display = Display(visible=0, size=(1024, 768))
display.start()
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

