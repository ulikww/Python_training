from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host = '127.0.0.1',name = 'address_in_groups', user = 'root', password = '')


def test_add_contact(app,db):
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="вспомогательная группа", header="вспомогательная группа", footer="вспомогательная группа"))
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik",
                                   company="1c",address="дмитровское ш 9", email="ulikwwwww@ya.ru"))
    def create_contact_to_group("//div[@class='right']/select//option[2]")
