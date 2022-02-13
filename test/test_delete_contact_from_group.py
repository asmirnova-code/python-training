from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app, orm, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TestName", lastname="Test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        contacts_list = db.get_contact_list()
        random_contact = random.choice(contacts_list)
        app.contact.assign_contact_by_id_to_group(random_contact.id, group.id)
        contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact.id, group.id)
    contacts_in_group = app.contact.get_contacts_in_group(group.id)
    db_contacts_in_group = orm.get_contacts_in_group(group)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(db_contacts_in_group, key=Contact.id_or_max)





