# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.Login(wd, username="admin", password="secret")
        self.Open_group_page(wd)
        self.Create_group(wd,Group(name= "dgdgdgd", header="dgdgdgd",footer= "dgdgdg"))
        self.Return_to_group_page(wd)
        self.Logout(wd)


    def test_add_ampty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.Login(wd, username="admin", password="secret")
        self.Open_group_page(wd)
        self.Create_group(wd,Group(name= "", header="",footer= ""))
        self.Return_to_group_page(wd)
        self.Logout(wd)

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def Return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def Create_group(self, wd, group):
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def Open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, username, password):
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
