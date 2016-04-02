
class GroupHelper:
        def __init__(self,app):
            self.app = app

        def Return_to_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

        def create(self, group):
            wd = self.app.wd
            self.open_group_page()
            # Init group creation
            wd.find_element_by_name("new").click()
            self.fill_group_form(group)
            # Submit group creation
            wd.find_element_by_name("submit").click()
            self.Return_to_group_page()

        def fill_group_form(self, group):
            wd = self.app.wd
            self.change_field_value("group_name",group.name)
            self.change_field_value("group_header",group.header)
            self.change_field_value("group_footer",group.footer)

        def change_field_value(self, field_name,text):
            wd = self.app.wd
            if text is not None:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

        def delete_first_group(self):
            wd = self.app.wd
            self.open_group_page()
            self.select_first_group()
            #submit deletion
            wd.find_element_by_name("delete").click()
            self.Return_to_group_page()

        def open_group_page(self):
            wd = self.app.wd
            if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
                wd.find_element_by_link_text("groups").click()


        def modification(self, group):
            wd = self.app.wd
            self.open_group_page()
            self.select_first_group()
            #submit modification group
            wd.find_element_by_name("edit").click()
            #modification group
            if group.Parent_group is not None:
                if not wd.find_element_by_name("group_parent_id").is_selected():
                    wd.find_element_by_name("group_parent_id").click()
                    wd.find_element_by_name("group_parent_id").send_keys(group.Parent_group)
            wd.find_element_by_name("update").click()




        def select_first_group(self):
            wd = self.app.wd
            wd.find_element_by_name("selected[]").click()


        def count(self):
            wd = self.app.wd
            self.open_group_page()
            return len(wd.find_elements_by_name("selected[]"))

