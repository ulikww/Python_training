from model.contact import Contact
from fixture.orm import ORMFixture

db = ORMFixture(host = '127.0.0.1',name = 'address_in_groups', user = 'root', password = '')

def test_add_contact(app, orm):
    old_contacts = orm.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik", company="1c",
                    address="дмитровское ш 9",
                    email="ulikwwwww@ya.ru"))
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts,key = Contact.id_or_max) == sorted(new_contacts,key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max )