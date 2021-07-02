'''
    Simple functions in Python to use Selenium resorces 
        in the majority of projects of Data Scraping.
'''

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def type_by_xpath(driver, xpath, texto):
    try:
    	driver.find_element_by_xpath(xpath).send_keys(texto)
    except NoSuchElementException:
        return False
    return True

def click_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(driver, classe):
    try:
        driver.find_elements_by_class_name(classe)
    except NoSuchElementException:
        return False
    return True

def catch_by_class(driver, classe,indice):
    return driver.find_elements_by_class_name(classe)[indice].text

def catch_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath).text

def catch_by_xpath_value(driver, xpath):
    return driver.find_element_by_xpath(xpath).get_attribute("value")

def clean_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath).clear()

def end_page(driver):
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)

def up_page(driver):
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_UP)