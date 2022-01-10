from model.contact import Contact

def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="New name"))

def test_edit_contact_birthday(app):
    app.contact.edit_first_contact(Contact(birthday="17"))