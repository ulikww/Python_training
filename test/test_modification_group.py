from model.group import Group

def test_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
        app.group.create(Group(name="родитель", header="родитель", footer="родитель"))
    old_groups = app.group.get_group_list()
    app.group.modification(Group(Parent_group="родитель"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key = Group.id_or_max)==sorted(new_groups, key = Group.id_or_max)

