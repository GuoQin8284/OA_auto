from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver():
    _auto_quit = None
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # cls._driver = webdriver.Ie()
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver and cls._auto_quit is not None:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def set_auto_quit(cls,auto_quit):
        cls._auto_quit = auto_quit
