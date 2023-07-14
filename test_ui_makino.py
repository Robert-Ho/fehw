from selenium import webdriver
from seleniumbase import BaseCase
from sbvt.visualtest import VisualTest

class Makino(BaseCase):
        
    def test_homepage(self):
        settings = {'projectToken': "N9e7XGvw/vZJYtpKZiLQ="}
        visualTest = VisualTest(self.driver, settings)
        url = "https://www.makino.com/"
        self.open(url)
        self.maximize_window()
        print(self.get_page_title())
        
        visualTest.capture("Home_Page",{'lazyload': 1000})

        self.click_link('Digital Makino')
        visualTest.capture("Digital_Makino_page",{'lazyload': 1000})

        self.click_link("Machine Technology")
        visualTest.capture("Machine_Technology_page",{'lazyload': 1000})

        