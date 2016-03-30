
class GroupHelper:
        def __init__(self,app):
            self.app = app

        def Return_to_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

        def create(self, group):
            wd = self.app.wd
            self.Open_group_page()
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
            self.Return_to_group_page()

        def delete_first_group(self):
            wd = self.app.wd
            self.Open_group_page()
            self.select_first_group()
            #submit deletion
            wd.find_element_by_name("delete").click()
            self.Return_to_group_page()

        def Open_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("groups").click()


        def modification(self, group):
            wd = self.app.wd
            self.Open_group_page()
            self.select_first_group()
            #submit modification group
            wd.find_element_by_name("edit").click()
            #modification group
            if group.Parent_group!="none":
                if not wd.find_element_by_xpath(group.Parent_group).is_selected():
                    wd.find_element_by_xpath(group.Parent_group).click()
            wd.find_element_by_name("update").click()


        def select_first_group(self):
            wd = self.app.wd
            wd.find_element_by_name("selected[]").click()

