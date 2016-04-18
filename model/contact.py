from sys import maxsize

class Contact:
    def __init__(self,firstname=None,middlename=None,lastname=None,nickname=None,company=None,
                 address=None,email=None,email2=None,email3=None,all_email_from_home_page=None,byear=None,bday=None,bmonth=None,
                 all_phones_from_home_page=None,id=None,mobilephone=None,homephone=None, secondaryphone=None,workphone=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.bday = bday
        self.bmonth = bmonth
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id,self.firstname,self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and\
               self.lastname == other.lastname



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
