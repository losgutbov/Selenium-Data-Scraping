from selenium import webdriver
from funcoes_comuns_selenium import *


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/losgutbov")
end_page(driver)
