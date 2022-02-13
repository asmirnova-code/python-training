from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TestName", lastname="Test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    contacts_list = db.get_contact_list()
    contact = random.choice(contacts_list)
    groups_list = db.get_group_list()
    group = random.choice(groups_list)
    app.contact.assign_contact_by_id_to_group(contact.id, group.id)
    contacts_in_group = app.contact.get_contacts_in_group(group.id)
    db_contacts_in_group = orm.get_contacts_in_group(group)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(db_contacts_in_group, key=Contact.id_or_max)

