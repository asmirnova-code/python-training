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

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, wd, firstname, middlename, lastname, nickname, title, company, address, home_phone,
                           mobile, work_home, fax, email, email2, email3, homepage, birthday, birthmonth, birthyear,
                           address2, house_number, notes):
        # fill first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        # fill middle name
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        # fill last name
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        # fill nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        # fill company
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        # fill address
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        # fill home phone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone)
        # fill mobile phone
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        # fill work phone
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work_home)
        # fill fax
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(fax)
        # fill email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        # fill email2
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        # fill email3
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        # fill homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        # select birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(birthday)
        wd.find_element_by_xpath("//option[@value='9']").click()
        # select birth month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(birthmonth)
        wd.find_element_by_xpath("//option[@value='August']").click()
        # fill birth year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birthyear)

        # fill address2
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address2)
        # fill house number
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(house_number)
        # fill notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_create_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_contact_page(wd)
        self.create_new_contact(wd, firstname="someone", middlename="dita", lastname="loren", nickname="pool",
                                title="research", company="cuberto", address="St. Petersburg",
                                home_phone="8974567", mobile="789234567899", work_home="234567889", fax="76834657",
                                email="email@somemail.com",
                                email2="dfghj@mail.com", email3="fghjkk@mail.com", homepage="address.com",
                                birthday="22", birthmonth="October", birthyear="1970",
                                address2="one address", house_number="15", notes="some notes")
        self.return_to_homepage(wd)
        self.logout(wd)

    def test_create_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_new_contact_page(wd)
        self.create_new_contact(wd, firstname="", middlename="", lastname="", nickname="",
                                title="", company="", address="",
                                home_phone="", mobile="", work_home="", fax="",
                                email="",
                                email2="", email3="", homepage="",
                                birthday="", birthmonth="", birthyear="",
                                address2="", house_number="", notes="")
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
