from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


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