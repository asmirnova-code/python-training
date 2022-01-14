from model.group import Group

def test_modify_empty_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name=""))
    else:
        if app.group.name() > 0:
            app.group.create(Group(name=""))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group7"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


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


