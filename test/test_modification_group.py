from model.group import Group
from random import randrange

def test_modification_some_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="dgdgdgd", header="dgdgdgd", footer="dgdgdg"))
        app.group.create(Group(name="родитель", header="родитель", footer="родитель"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    app.group.modification_group_by_index(index, Group(Parent_group="родитель"))
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key = Group.id_or_max)==sorted(new_groups, key = Group.id_or_max)

