
from model.contact import Contact


def test_modification_contact(app):
    app.contact.modification(Contact(bday="//div[@id='content']/form[1]/select[1]//option[7]",byear="1990",bmonth="//div[@id='content']/form[1]/select[2]//option[3]"))
