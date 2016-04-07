from model.group import Group

def test_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
        app.group.create(Group(name="родитель", header="родитель", footer="родитель"))
    old_groups = app.group.get_group_list()
    app.group.modification(Group(Parent_group="родитель"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key = Group.id_or_max)==sorted(new_groups, key = Group.id_or_max)

