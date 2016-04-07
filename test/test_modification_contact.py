from model.contact import Contact
from random import randrange


def test_modification_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
         app.contact.create(Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik", company="1c", address="дмитровское ш 9",
                               email="ulikwwwww@ya.ru"))
    index = randrange(len(old_contacts))
    app.contact.modification_contact_by_index(index, Contact(bday="//div[@id='content']/form[1]/select[1]//option[7]",byear="1990",bmonth="//div[@id='content']/form[1]/select[2]//option[3]"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key = Contact.id_or_max)==sorted(new_contacts, key = Contact.id_or_max)