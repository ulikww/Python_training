from model.group import Group

def test_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
        app.group.create(Group(name="родитель", header="родитель", footer="родитель"))
    old_groups = app.group.get_group_list()
    group = Group(Parent_group="родитель")
    group.id = old_groups[0].id
    app.group.modification(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max)==sorted(new_groups, key = Group.id_or_max)

