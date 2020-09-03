from selenium import webdriver
import time
import unittest
import random
import math
class SignIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('E:\minor_projects\Automation Testing by Selenium\chromedriver.exe')

    def test_login_valid(self):
        #valid username and password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element_by_class_name("_2zrpKA").send_keys("7351650033")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()


    def test_login_invalid_password(self):
        #In valid password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element_by_class_name("_2zrpKA").send_keys("7351650033")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("para")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'Your username or password is incorrect'
        self.driver.implicitly_wait(10)
        temp = self.driver.find_element_by_class_name('ZAtlA-').get_attribute('innerHTML')
        error_msg_got = temp.lstrip("<span>")
        error_msg_got = error_msg_got.rstrip("</span>")
        self.assertEqual(error_msg_got,error_msg_actual)


    def test_login_invalid_username(self):
        #In valid username
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element_by_class_name("_2zrpKA").send_keys("parasgulati7100@gmail.com")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'You are not registered with us. Please sign up.'
        self.driver.implicitly_wait(5)
        error_msg_got = self.driver.find_element_by_class_name('JAUzCh').get_attribute('innerHTML')
        self.assertEqual(error_msg_got, error_msg_actual)


    def test_login_invalid_username_password(self):
        #In valid username and password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element_by_class_name("_2zrpKA").send_keys("parasgulati7100@gmail.com")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("paral")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'You are not registered with us. Please sign up.'
        self.driver.implicitly_wait(5)
        error_msg_got = self.driver.find_element_by_class_name('JAUzCh').get_attribute('innerHTML')
        self.assertEqual(error_msg_got, error_msg_actual)

    def test_login_invalid_username_specialSymbol(self):
        #In valid special symbol in username
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element_by_class_name("_2zrpKA").send_keys("@#parasgulati&^...")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'Please enter valid Email ID/Mobile number'
        self.driver.implicitly_wait(10)
        temp = self.driver.find_element_by_class_name('ZAtlA-').get_attribute('innerHTML')
        error_msg_got = temp.lstrip("<span>")
        error_msg_got = error_msg_got.rstrip("</span>")
        self.assertEqual(error_msg_got, error_msg_actual)


    def test_login_invalid_large_length_username_or_password(self):
        #large_length_username_or_password
        input = 'pafrdddhdngirmcspdfgkrkfa'*100
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element_by_class_name("_2zrpKA").send_keys(input)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys(input)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'Please enter valid Email ID/Mobile number'
        self.driver.implicitly_wait(10)
        temp = self.driver.find_element_by_class_name('ZAtlA-').get_attribute('innerHTML')
        error_msg_got = temp.lstrip("<span>")
        error_msg_got = error_msg_got.rstrip("</span>")
        self.assertEqual(error_msg_got, error_msg_actual)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
