import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_name_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/') 
    time.sleep(30)
    button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
    )
    
    assert button != None, 'Button "Add to basket" not found.'