from model.contact import Contact

def test_edit_contact_empty_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname=""))
    else:
        if app.contact.lastname() > 0:
            app.contact.create(Contact(lastname=""))
    app.contact.edit_first_contact(Contact(lastname="New name3"))

def test_edit_contact_birthday(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname="Test name", birthday="-"))
    app.contact.edit_first_contact(Contact(birthday="17"))