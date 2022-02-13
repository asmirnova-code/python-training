from model.contact import Contact
import random

def test_add_contact_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TestName", lastname="Test"))
    # get contacts list from db
    contacts_list = db.get_contact_list()
    # select random contact
    contact = random.choice(contacts_list)
    # get groups list from db
    groups_list = db.get_group_list()
    # select random group
    group = random.choice(groups_list)
    # assign contact to group
    app.contact.assign_contact_by_id_to_group(contact.id, group.id)
    # get contacts in selected group
    contacts_in_group = app.contact.get_contacts_in_group(group.id)
    # get contacts in selected group in db
    db_contacts_in_group = orm.get_contacts_in_group(group)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(db_contacts_in_group, key=Contact.id_or_max)

