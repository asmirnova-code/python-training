from model.group import Group
from random import randrange

def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="GroupName"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group7")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_empty_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    else:
        if app.group.name() > 0:
            app.group.create(Group(name=""))
    old_groups = app.group.get_group_list()
    group = Group(name="New group7")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_group_name_to_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group name"))
    else:
        if app.group.name() == 0:
            app.group.create(Group(name="Group name"))
            old_groups = app.group.get_group_list()
            app.group.modify_last_group(Group(name=""))
            new_groups = app.group.get_group_list()
            assert len(old_groups) == len(new_groups)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_empty_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header=""))
    else:
        if app.group.header() > 0:
            app.group.create(Group(header=""))
            old_groups = app.group.get_group_list()
            app.group.modify_last_group(Group(header="New header23"))
            new_groups = app.group.get_group_list()
            assert len(old_groups) == len(new_groups)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header70"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


