
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Chrome()
driver.get('https://www.bing.com/')


def click_button (button_name):
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_name))).click()
    except:
        raise NoSuchElementException

def type_text (field_name, text):
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, field_name)))
        field = driver.find_element(By.XPATH, field_name)
        field.send_keys(text)
    except:
        raise NoSuchElementException

def selection_randomizer ():
    closes_list = 'news in ukraine', 'weather in melrose', 'android news', 'RPI highlights'
    return (random.choices(closes_list, k=1))

