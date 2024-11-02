import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_browser_language_and_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    basket_button=browser.find_elements(By.XPATH, '//form[@id="add_to_basket_form"]/button')
    assert len(basket_button) >0, 'Не найдена кнопка добавления в корзину'
    time.sleep(30)


