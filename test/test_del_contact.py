from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="TestName", lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


