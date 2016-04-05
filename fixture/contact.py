from model.contact import Contact


class ContactHelper:
    def __init__(self,app):
            self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname",contact.firstname)
        self.change_field_value_contact("middlename",contact.middlename)
        self.change_field_value_contact("lastname",contact.lastname)
        self.change_field_value_contact("nickname",contact.nickname)
        self.change_field_value_contact("company",contact.company)
        self.change_field_value_contact("address",contact.address)
        self.change_field_value_contact("email",contact.email)

    def change_field_value_contact(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        #confirm the deletion
        wd.switch_to_alert().accept()

    def open_contact_list(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modification(self, contact):
        wd = self.app.wd
        self.open_contact_list()
        self.select_first_contact()
        #modification contact
        wd.find_element_by_css_selector("td.center:nth-child(8) > a:nth-child(1) > img:nth-child(1)").click()
        self.drop_down_list(contact.bday)
        self.drop_down_list(contact.bmonth)
        self.change_field_value_contact("byear",contact.byear)
        wd.find_element_by_name("update").click()

    def drop_down_list(self, text):
         wd = self.app.wd
         if text is not None:
            if not wd.find_element_by_xpath(text).is_selected():
                wd.find_element_by_xpath(text).click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_list()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                contacts.append(Contact(lastname=text,id=id))
        return contacts









