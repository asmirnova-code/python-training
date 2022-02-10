from model.group import Group
import random

def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="GroupName"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    new_test_group = Group(name="New group7")
    new_test_group.id = random_group.id
    app.group.modify_group_by_id(random_group.id, new_test_group)
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    old_groups.append(new_test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



#def test_modify_empty_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name=""))
#    else:
#        if app.group.name() > 0:
#           app.group.create(Group(name=""))
#    old_groups = app.group.get_group_list()
#    group = Group(name="New group7")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_group_name_to_empty(app):
#    if app.group.count() == 0:
#       app.group.create(Group(name="Group name"))
#    else:
#        if app.group.name() == 0:
#            app.group.create(Group(name="Group name"))
#            old_groups = app.group.get_group_list()
#            app.group.modify_last_group(Group(name=""))
#            new_groups = app.group.get_group_list()
#           assert len(old_groups) == len(new_groups)
#   old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name=""))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)


#def test_modify_empty_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header=""))
#    else:
#        if app.group.header() > 0:
#            app.group.create(Group(header=""))
#            old_groups = app.group.get_group_list()
#           app.group.modify_last_group(Group(header="New header23"))
#            new_groups = app.group.get_group_list()
#            assert len(old_groups) == len(new_groups)
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header70"))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)


