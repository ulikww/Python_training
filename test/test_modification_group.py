from model.group import Group

def test_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
        app.group.create(Group(name="родитель", header="родитель", footer="родитель"))
    app.group.modification(Group(Parent_group="родитель"))
