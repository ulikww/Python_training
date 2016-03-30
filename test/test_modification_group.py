from model.group import Group

def test_modification(app):
    app.group.modification(Group(Parent_group="//div[@id='content']//select[normalize-space(.)='родитель [none]']//option[1]"))
