# -*- coding: utf-8 -*-

import pytest
from fixture.application_c import application_c
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = application_c()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.Login(username="admin",password="secret")
    app.create_contact(Contact(firstname="Ульяна",middlename= "Владимировна", lastname="Ватракшина",nickname= "ulik",company= "1c",adress= "дмитровское ш 9",
                        email="ulikwwwww@ya.ru"))
    app.session.Logout()
def test_add__empty_contact(app):
    app.session.Login(username="admin",password="secret")
    app.create_contact(Contact(firstname="",middlename= "", lastname="",nickname= "",company= "",adress= "",
                            email=""))
    app.session.Logout()




