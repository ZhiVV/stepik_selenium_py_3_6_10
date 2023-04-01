import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_name_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/') 
    time.sleep(10)
    
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert len(button) > 0, 'Button "Add to basket" not found.'
    assert len(button) < 2, 'Button "Add to basket" more than one.'