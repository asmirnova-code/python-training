from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_delete_two_groups(app):
    if app.group.count() < 2:
        for i in range(2):
            app.group.create(Group(name="Group3"))
    old_groups = app.group.get_group_list()
    app.group.delete_two_groups()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 2 == len(new_groups)