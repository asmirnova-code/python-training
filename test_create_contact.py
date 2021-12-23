# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestCreateContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, wd):
        # fill first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("someone")
        # fill middle name
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("dita")
        # fill last name
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("loren")
        # fill nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("pool")
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("research")
        # fill company
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("cuberto")
        # fill address
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("St. Petersburg")
        # fill home phone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("8974567")
        # fill mobile phone
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("789234567899")
        # fill work phone
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("234567889")
        # fill fax
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("76834657")
        # fill email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@somemail.com")
        # fill email2
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("dfghj@mail.com")
        # fill email3
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("fghjkk@mail.com")
        # fill homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("address.com")
        # select birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("9")
        wd.find_element_by_xpath("//option[@value='9']").click()
        # select birth month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        wd.find_element_by_xpath("//option[@value='August']").click()
        # fill birth year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1970")
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("9")
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[11]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[9]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1970")
        # fill address2
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("one address")
        # fill house number
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("15")
        # fill notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("some notes")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_create_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_new_contact_page(wd)
        self.create_new_contact(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
