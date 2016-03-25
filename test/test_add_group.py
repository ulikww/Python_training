# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
    app.session.Logout()


def test_add_ampty_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.Logout()
