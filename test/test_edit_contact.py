from model.contact import Contact

def test_edit_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New name"))
    app.session.logout()

def test_edit_contact_birthday(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(birthday="17"))
    app.session.logout()