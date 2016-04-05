class Contact:
    def __init__(self,firstname=None,middlename=None,lastname=None,nickname=None,company=None,address=None,email=None,byear=None,bday=None,bmonth=None,id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.email = email
        self.byear = byear
        self.bday = bday
        self.bmonth = bmonth
        self.id = id


    def __repr__(self):
        return "%s:%s" % (self.id,self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.lastname == other.lastname
