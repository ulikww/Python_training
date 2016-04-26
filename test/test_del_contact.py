from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="человек"))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts)-1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert new_contacts == app.contact.get_contact_list()