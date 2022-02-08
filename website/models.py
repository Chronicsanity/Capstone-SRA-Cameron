from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    role = db.Column(db.String(150))


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tnumber = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150))
    middlename = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    term = db.Column(db.String(150))
    level = db.Column(db.String(150))
    pprogram = db.Column(db.String(150))
    ppname = db.Column(db.String(150))
    pcollege = db.Column(db.String(150))
    pdept = db.Column(db.String(150))
    pdeptdesc = db.Column(db.String(150))
    sprogram = db.Column(db.String(150))
    spname = db.Column(db.String(150))
    scollege = db.Column(db.String(150))
    sdept = db.Column(db.String(150))
    sdeptdesc = db.Column(db.String(150))
    decision = db.Column(db.String(150))
    admit = db.Column(db.Date())
    saddress1 = db.Column(db.String(150))
    saddress2 = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    zip = db.Column(db.String(150))
    phonearea = db.Column(db.String(150))
    phonenum = db.Column(db.String(150))
    phonenumex = db.Column(db.String(150))
    email = db.Column(db.String(150))
    ualremail = db.Column(db.String(150))
    ethnicity = db.Column(db.String(150))
    sex = db.Column(db.String(150))
    admission = db.Column(db.String(150))
    studenttype = db.Column(db.String(150))

class ImportData(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tnumber = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150))
    middlename = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    term = db.Column(db.String(150))
    level = db.Column(db.String(150))
    pprogram = db.Column(db.String(150))
    ppname = db.Column(db.String(150))
    pcollege = db.Column(db.String(150))
    pdept = db.Column(db.String(150))
    pdeptdesc = db.Column(db.String(150))
    decision = db.Column(db.String(150))
    admit = db.Column(db.Date())
    saddress1 = db.Column(db.String(150))
    saddress2 = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    zip = db.Column(db.String(150))
    phonearea = db.Column(db.String(150))
    phonenum = db.Column(db.String(150))
    phonenumex = db.Column(db.String(150))
    email = db.Column(db.String(150))
    ualremail = db.Column(db.String(150))
    studenttype = db.Column(db.String(150))
class callingData(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tnumber = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150))
    middlename = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    term = db.Column(db.String(150))
    level = db.Column(db.String(150))
    pprogram = db.Column(db.String(150))
    ppname = db.Column(db.String(150))
    pcollege = db.Column(db.String(150))
    pdept = db.Column(db.String(150))
    admit = db.Column(db.Date())
    saddress1 = db.Column(db.String(150))
    saddress2 = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    zip = db.Column(db.String(150))
    phonearea = db.Column(db.String(150))
    phonenum = db.Column(db.String(150))
    phonenumex = db.Column(db.String(150))
    email = db.Column(db.String(150))
    ualremail = db.Column(db.String(150))
    studenttype = db.Column(db.String(150))
    campaign = db.Column(db.String(150))
    campaignyear = db.Column(db.Integer)
    wascalled = db.Column(db.String(150))
    caller = db.Column(db.String(150))
    datecalled = (db.Date())
    numbertimescalled = db.Column(db.Integer)
    calldisposition = db.Column(db.String(150))
    callnotes = db.Column(db.String(150))
    wasemailed = db.Column(db.Boolean)
    dateemailed = (db.Date())
    email = db.Column(db.String(150))
    hascaller = db.Column(db.String(150))