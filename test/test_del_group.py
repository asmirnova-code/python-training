from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.delete_first_group()


def test_delete_two_groups(app):
    if app.group.count() < 2:
        for i in range(2):
            app.group.create(Group(name="Group3"))
    app.group.delete_two_groups()