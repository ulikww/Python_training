from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company="", address="",email="")] + [
        Contact(firstname="Ульяна", middlename="Владимировна", lastname="Ватракшина", nickname="ulik", company="1c",
        address="дмитровское ш 9",email="ulikwwwww@ya.ru", homephone="3434343", mobilephone="4454545", workphone="657676",
        secondaryphone="88888")] +[Contact(firstname=random_string("firstname",23),middlename=random_string("middlename",24),
                                           lastname=random_string("lastname",8))]
