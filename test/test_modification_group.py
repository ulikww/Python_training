from model.group import Group

def test_modification(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
        app.group.create(Group(name="родитель", header="родитель", footer="родитель"))
    app.group.modification(Group(Parent_group="родитель"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
