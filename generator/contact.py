from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits + " "*5
    number = "".join([random.choice(symbols) for i in range(maxlen)])
    return prefix + "+7{}".format(number)


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    email = "".join([random.choice(symbols) for i in range(maxlen)])
    return prefix + "{}@gmail.com".format(email)


def random_byear():
    return str(random.randint(1900, 2022))


def random_bday():
    return str(random.randint(1, 31))


def random_month():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October',
                  'November', 'December']
    return random.choice(month_list)



testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                      home_phone="", mobile="", work_phone="", fax="", email="", email2="", email3="", homepage="",
                      birthday="-", birthmonth="-", birthyear="", address2="", secondary_phone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
            home_phone=random_phone("home_phone", 10), mobile=random_phone("mobile", 10),
            work_phone=random_phone("work_phone", 10), fax=random_phone("fax", 10),
            email=random_email("email", 6),
            email2=random_email("email2", 6), email3=random_email("email3", 6), homepage="address.com",
            birthday=random_bday(),
            birthmonth=random_month(), birthyear=random_byear(), address2=random_string("address", 10),
            secondary_phone=random_phone("secondary_phone", 10), notes=random_string("notes", 60))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",  f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))