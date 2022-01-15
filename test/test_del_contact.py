from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


