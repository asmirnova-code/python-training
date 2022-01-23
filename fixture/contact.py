from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and
        len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))) > 0:
            wd.get("http://localhost/addressbook/index.php")

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill first name
        self.change_field_value("firstname", contact.firstname)
        # fill middle name
        self.change_field_value("middlename", contact.middlename)
        # fill last name
        self.change_field_value("lastname", contact.lastname)
        # fill nickname
        self.change_field_value("nickname", contact.nickname)
        # fill title
        self.change_field_value("title", contact.title)
        # fill company
        self.change_field_value("company", contact.company)
        # fill address
        self.change_field_value("address", contact.address)
        # fill home phone
        self.change_field_value("home", contact.home_phone)
        # fill mobile phone
        self.change_field_value("mobile", contact.mobile)
        # fill work phone
        self.change_field_value("work", contact.work_phone)
        # fill fax
        self.change_field_value("fax", contact.fax)
        # fill email
        self.change_field_value("email", contact.email)
        # fill email2
        self.change_field_value("email2", contact.email2)
        # fill email3
        self.change_field_value("email3", contact.email3)
        # fill homepage
        self.change_field_value("homepage", contact.homepage)
        # select birthday
        self.change_dropdown_value("bday", contact.birthday)
        # select birth month
        self.change_dropdown_value("bmonth", contact.birthmonth)
        # fill birth year
        self.change_field_value("byear", contact.birthyear)
        # fill address2
        self.change_field_value("address2", contact.address2)
        # fill home
        self.change_field_value("phone2", contact.home)
        # fill notes
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, data):
        wd = self.app.wd
        if data is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(data)
            wd.find_element_by_xpath("//option[@value='" + data + "']").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit creation
        wd.find_element_by_name("submit").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        # open home page
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # click edit button
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        # open home page
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_homepage()
        self.contact_cache = None


    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count_contact(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def lastname(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        element = wd.find_element_by_name("lastname").get_attribute("value")
        return len(element)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)







