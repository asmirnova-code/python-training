from model.contact import Contact

def test_edit_contact_empty_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname=""))
    else:
        if app.contact.lastname() > 0:
            app.contact.create(Contact(lastname=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="loren")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_contact_birthday(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(lastname="Test name", birthday="-"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="someone", middlename="dita", lastname="loren", nickname="pool",
                      title="research", company="cuberto", address="St. Petersburg",
                      home_phone="8974567", mobile="789234567899", work_phone="234567889", fax="76834657",
                      email="email@somemail.com",
                      email2="dfghj@mail.com", email3="fghjkk@mail.com", homepage="address.com",
                      birthday="2", birthmonth="November", birthyear="1970",
                      address2="one address", home="15", notes="some notes")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(Contact(birthday="17"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)