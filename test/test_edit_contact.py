from model.contact import Contact

def test_edit_contact_empty_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname=""))
    else:
        if app.contact.lastname() > 0:
            app.contact.create(Contact(lastname=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname="New name3"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_contact_birthday(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname="Test name", birthday="-"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(birthday="17"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)