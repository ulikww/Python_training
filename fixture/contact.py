from model.contact import Contact
import re

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
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname",contact.firstname)
        self.change_field_value_contact("middlename",contact.middlename)
        self.change_field_value_contact("lastname",contact.lastname)
        self.change_field_value_contact("nickname",contact.nickname)
        self.change_field_value_contact("company",contact.company)
        self.change_field_value_contact("address",contact.address)
        self.change_field_value_contact("email",contact.email)
        self.change_field_value_contact("home",contact.homephone)
        self.change_field_value_contact("mobile",contact.mobilephone)
        self.change_field_value_contact("phone2",contact.secondaryphone)
        self.change_field_value_contact("work",contact.workphone)

    def change_field_value_contact(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        #confirm the deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def delete_contact_by_id(self,id):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_id(id)
        #submit deletion
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        #confirm the deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def open_contact_list(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modification(self):
        self.modification_contact_by_index(0)

    def modification_contact_by_index(self,index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.drop_down_list(contact.bday)
        self.drop_down_list(contact.bmonth)
        self.change_field_value_contact("byear",contact.byear)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modification_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.drop_down_list(contact.bday)
        self.drop_down_list(contact.bmonth)
        self.change_field_value_contact("byear", contact.byear)
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def drop_down_list(self, text):
         wd = self.app.wd
         if text is not None:
            if not wd.find_element_by_xpath(text).is_selected():
                wd.find_element_by_xpath(text).click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                td_cells = element.find_elements_by_tag_name("td")
                first = td_cells[2].text
                last = td_cells[1].text
                all_phones = td_cells[5].text
                all_email =td_cells[4].text
                address = td_cells[3].text
                self.contact_cache.append(Contact(lastname=last,firstname=first,id=id,address=address, all_phones_from_home_page = all_phones, all_email_from_home_page = all_email))
        return list(self.contact_cache)



    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_list()
        row = wd.find_element_by_name("selected[]").get_attribute("value")[int(id)]
        #row =rows[int(id)]
        #row = wd.find_element_by_css_selector("input[value='%s']" % id)
        cells = row.find_elements_by_tag_name("td")
        cell = cells[7]
        cell.find_element_by_tag_name("a").click()



    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        adress = wd.find_element_by_css_selector("#content > form:nth-child(2) > textarea:nth-child(30)").text
        return Contact(firstname = firstname,lastname = lastname,id = id,
                       homephone = homephone,workphone = workphone,mobilephone = mobilephone,
                       secondaryphone = secondaryphone,email = email, email2 = email2, email3 = email3,address=adress)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone = homephone,workphone = workphone,mobilephone = mobilephone,
                       secondaryphone = secondaryphone)











