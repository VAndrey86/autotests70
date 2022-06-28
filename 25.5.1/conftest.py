from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\\WebDriver\\bin\\chromedriver.exe')

   pytest.driver.set_window_size(1400, 1000)
   # Переходим на страhttps://petfriends.skillfactory.ru/login')

   yield


   pytest.driver.quit()
