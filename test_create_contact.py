# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        # open home page
        driver.get("http://localhost/addressbook/edit.php")
        # login
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        # fill first name
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("someone")
        # fill middle name
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("dita")
        # fill last name
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("loren")
        # fill nickname
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("pool")
        # fill title
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("research")
        # fill company
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("cuberto")
        # fill address
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("St. Petersburg")
        # fill home phone
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("8974567")
        # fill mobile phone
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("789234567899")
        # fill work phone
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("234567889")
        # fill fax
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("76834657")
        # fill email
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("email@somemail.com")
        # fill email2
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("dfghj@mail.com")
        # fill email3
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("fghjkk@mail.com")
        # fill homepage
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("address.com")
        # select birthday
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("9")
        driver.find_element_by_xpath("//option[@value='9']").click()
        # select birth month
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("August")
        driver.find_element_by_xpath("//option[@value='August']").click()
        # fill birth year
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1970")
        driver.find_element_by_name("aday").click()
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("9")
        driver.find_element_by_xpath("//div[@id='content']/form/select[3]/option[11]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("August")
        driver.find_element_by_xpath("//div[@id='content']/form/select[4]/option[9]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("1970")
        # fill address2
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("one address")
        # fill house number
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("15")
        # fill notes
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("some notes")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to the homepage
        driver.find_element_by_link_text("home page").click()
        # logout
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
