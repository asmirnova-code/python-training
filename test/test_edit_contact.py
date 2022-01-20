from model.contact import Contact

def test_edit_contact_empty_lastname(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="some", middlename="dita", lastname="", nickname="pool",
    title="research", company="cuberto", address="St. Petersburg", home_phone="8974567", mobile="789234567899",
    work_phone="234567889", fax="76834657", email="email@somemail.com", email2="dfghj@mail.com",
    email3="fghjkk@mail.com", homepage="address.com", birthday="15", birthmonth="November", birthyear="1970",
    address2="one address", home="15", notes="some notes"))
    else:
        if app.contact.lastname() > 0:
            app.contact.create(Contact(firstname="some", middlename="dita", lastname="", nickname="pool",
    title="research", company="cuberto", address="St. Petersburg", home_phone="8974567", mobile="789234567899",
    work_phone="234567889", fax="76834657", email="email@somemail.com", email2="dfghj@mail.com",
    email3="fghjkk@mail.com", homepage="address.com", birthday="15", birthmonth="November", birthyear="1970",
    address2="one address", home="15", notes="some notes"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="some", lastname="edited")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_contact_firstname(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="name", middlename="dita", lastname="loren", nickname="pool",
    title="research", company="cuberto", address="St. Petersburg", home_phone="8974567", mobile="789234567899",
    work_phone="234567889", fax="76834657", email="email@somemail.com", email2="dfghj@mail.com",
    email3="fghjkk@mail.com", homepage="address.com", birthday="15", birthmonth="November", birthyear="1970",
    address2="one address", home="15", notes="some notes"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="edited", lastname="loren")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)