import pytest
from model.contact import Contact

def test_create_contact(app):
    app.contact.create(Contact(firstname="someone", middlename="dita", lastname="loren", nickname="pool",
                               title="research", company="cuberto", address="St. Petersburg",
                               home_phone="8974567", mobile="789234567899", work_phone="234567889", fax="76834657",
                               email="email@somemail.com",
                               email2="dfghj@mail.com", email3="fghjkk@mail.com", homepage="address.com",
                               birthday="2", birthmonth="November", birthyear="1970",
                               address2="one address", home="15", notes="some notes"))


def test_create_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="",
                               home_phone="", mobile="", work_phone="", fax="",
                               email="",
                               email2="", email3="", homepage="",
                               birthday="", birthmonth="-", birthyear="",
                               address2="", home="", notes=""))


