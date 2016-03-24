# -*- coding: utf-8 -*-

import pytest
from fixture.application import application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_group(app):
    app.Login(username="admin", password="secret")
    app.Create_group(Group(name= "dgdgdgd", header="dgdgdgd",footer= "dgdgdg"))
    app.Logout()


def test_add_ampty_group(app):
    app.Login(username="admin", password="secret")
    app.Create_group(Group(name= "", header="",footer= ""))
    app.Logout()
