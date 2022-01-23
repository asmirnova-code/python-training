from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


# def test_delete_two_groups(app):
#    if app.group.count() < 2:
#        for i in range(2):
#            app.group.create(Group(name="Group3"))
#    old_groups = app.group.get_group_list()
#    app.group.delete_two_groups()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 2 == len(new_groups)
#    old_groups[0:2] = []
#    assert old_groups == new_groups