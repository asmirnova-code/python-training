from model.contact import Contact
from random import randrange
import re


def test_all_contacts_ui_db(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="TestName", lastname="Test", address="St.Petersburg 15",
                                   home_phone="8974567", mobile="789234567899",  work_phone="234567889", fax="76834657",
                                   email="email@somemail.com", email2="dfghj@mail.com", email3="fghjkk@mail.com",
                                   birthday="15", birthmonth="November", birthyear="1970", address2="one address",
                                   secondary_phone="15", notes="some notes" ))
    contacts_from_home_page = app.contact.get_contact_list()
    db_contacts = map(clean, orm.get_contact_list())
    assert sorted(db_contacts, key=Contact.id_or_max) == sorted(contacts_from_home_page, key=Contact.id_or_max)
    for contact in contacts_from_home_page:
        assert contact.firstname == orm.get_contact_by_id(contact.id).firstname
        assert contact.lastname == orm.get_contact_by_id(contact.id).lastname
        assert contact.address == orm.get_contact_by_id(contact.id).address
        assert contact.all_email_from_home_page == merge_email_like_on_home_page(orm.get_contact_by_id(contact.id))
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(orm.get_contact_by_id(contact.id))


def test_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="TestName", lastname="Test", address="St.Petersburg 15",
                                   home_phone="8974567", mobile="789234567899",  work_phone="234567889", fax="76834657",
                                   email="email@somemail.com", email2="dfghj@mail.com", email3="fghjkk@mail.com",
                                   birthday="15", birthmonth="November", birthyear="1970", address2="one address",
                                   secondary_phone="15", notes="some notes" ))
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                    [contact.home_phone, contact.mobile, contact.work_phone, contact.secondary_phone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def clean(contact):
    return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                   address=contact.address.strip())