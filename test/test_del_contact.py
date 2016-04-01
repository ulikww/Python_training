from model.contact import Contact

def test_delete_firt_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="человек"))
    app.contact.delete_first_contact()