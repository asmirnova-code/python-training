from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="edit2", middlename="edit", lastname="edit", nickname="pool",
                               title="research", company="cuberto", address="St. Petersburg",
                               home_phone="8974567", mobile="789234567899", work_phone="234567889", fax="76834657",
                               email="email@somemail.com",
                               email2="dfghj@mail.com", email3="fghjkk@mail.com", homepage="address.com",
                               birthday="2", birthmonth="November", birthyear="1970",
                               address2="one address", home="15", notes="some notes"))
    app.session.logout()