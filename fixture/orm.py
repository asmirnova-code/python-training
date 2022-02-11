from pony.orm import *
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class ORMFixture():
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        middlename = Optional(str, column='middlename')
        nickname = Optional(str, column='nickname')
        title = Optional(str, column='title')
        company = Optional(str, column='company')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        birthday = Optional(str, column='bday')
        birthmonth = Optional(str, column='bmonth')
        birthyear = Optional(str, column='byear')
        address2 = Optional(str, column='address2')
        notes = Optional(str, column='notes')
        secondary_phone = Optional(str, column='phone2')
        deprecated = Optional(str, column='deprecated')


    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, middlename=contact.middlename,
                           nickname=contact.nickname, title=contact.title, company=contact.company, address=contact.address,
                           home_phone=contact.home_phone, mobile=contact.mobile, work_phone=contact.work_phone,
                           fax=contact.fax, email=contact.email, email2=contact.email2, email3=contact.email3,
                           homepage=contact.homepage, birthday=contact.birthday, birthmonth=contact.birthmonth,
                           birthyear=contact.birthyear, address2=contact.address2, secondary_phone=contact.secondary_phone,
                           notes=contact.notes)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))