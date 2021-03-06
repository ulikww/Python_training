from model.contact import Contact
import random


def test_modification_some_contact(app, db,check_ui):
    old_contacts = db.get_contact_list()
    if app.contact.count() == 0:
         app.contact.create(Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik", company="1c", address="дмитровское ш 9",
                               email="ulikwwwww@ya.ru"))
    contact = random.choice(old_contacts)
    app.contact.modification_contact_by_id(contact.id, Contact(bday="//div[@id='content']/form[1]/select[1]//option[7]",byear="1990",bmonth="//div[@id='content']/form[1]/select[2]//option[3]"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key = Contact.id_or_max)==sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(),key = Contact.id_or_max)