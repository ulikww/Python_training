
class ContactHelper:
    def __init__(self,app):
            self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.adress)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        #confirm the deletion
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modification(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        #modification contact
        wd.find_element_by_css_selector("td.center:nth-child(8) > a:nth-child(1) > img:nth-child(1)").click()

        if contact.bday != "":
            if not wd.find_element_by_xpath(contact.bday).is_selected():
                wd.find_element_by_xpath(contact.bday).click()
        if contact.bmonth !="":
            if not wd.find_element_by_xpath(contact.bmonth).is_selected():
                wd.find_element_by_xpath(contact.bmonth).click()
        if contact.byear != "":
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("update").click()







