class Contact(object):

    def __init__(self, fName, lName, email, phone):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.phone = phone

    def getfName(self):
        return self.fName
    def getlName(self):
        return self.lName
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone

    def __str__(self):
        return "%s %s %s %s" % (self.fName, self.lName, self.email, self.phone)
