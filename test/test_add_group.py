# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
    app.group.create(Group(name="родитель", header="родитель", footer="родитель"))


def test_add_ampty_group(app):
    app.group.create(Group(name="", header="", footer=""))


