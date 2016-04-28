from model.contact import Contact
from  model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host = '127.0.0.1',name = 'addressbook', user = 'root', password = '')


def test_del_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="вспомогательная группа", header="вспомогательная группа", footer="вспомогательная группа"))
    if len(old_contacts) == 0:
        app.contact.create(
            Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik", company="1c",
                    address="дмитровское ш 9",email="ulikwwwww@ya.ru",group_in_contact="//div[@id='content']/form/select[5]//option[2]"))
    contacts_in_group = db.get_contact_in_groups()
    if len(contacts_in_group) != 0:
        contact = random.choice(contacts_in_group)
        app.contact.remove_contact_from_group(contact)
        #app.contact.remove_contact_from_group(contact.group_in_contact)




     #if new_contacts

    #contact = random.choice(old_contacts.group_in_contact)
    #app.contact.delete_contact_by_id(contact.id)
    #old_contacts.remove(contact)
        #new_contacts = db.get_contact_list()
        #old_contacts.append(contact)
        #assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key = Contact.id_or_max)
        #if check_ui:
     #   assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max )
