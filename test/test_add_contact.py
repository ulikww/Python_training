# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik", company="1c", adress="дмитровское ш 9",
                       email="ulikwwwww@ya.ru"))

def test_add__empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", company="", adress="",
                       email=""))





