# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture import Fixture

@pytest.fixture
def app(request):
    fixture = Fixture()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="someone", middlename="dita", lastname="loren", nickname="pool",
                                title="research", company="cuberto", address="St. Petersburg",
                                home_phone="8974567", mobile="789234567899", work_phone="234567889", fax="76834657",
                                email="email@somemail.com",
                                email2="dfghj@mail.com", email3="fghjkk@mail.com", homepage="address.com",
                                birthday="2", birthmonth="November", birthyear="1970",
                                address2="one address", home="15", notes="some notes"))
    app.logout()

def test_create_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                                title="", company="", address="",
                                home_phone="", mobile="", work_phone="", fax="",
                                email="",
                                email2="", email3="", homepage="",
                                birthday="", birthmonth="-", birthyear="",
                                address2="", home="", notes=""))

    app.logout()

