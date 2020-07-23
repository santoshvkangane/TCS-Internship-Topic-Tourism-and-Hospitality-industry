from django.db import models

# Create your models here.
from requests import options


class Signup2(models.Model):
    objects = None
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    class Meta:
        db_table = "signup2"


class Registration2(models.Model):
    objects = None
    name = models.CharField(max_length=30)
    age = models.FloatField(max_length=10)
    contact = models.IntegerField()
    address = models.CharField(max_length=30)

    class Meta:
        db_table = "registration2"


class Eventreg(models.Model):
    objects = None
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    EmailId = models.EmailField(max_length=100)
    ENAME_CHOICES = (
        ("DIWALI", "DIWALI"),
        ("GUDHI PADWA", "GUDHI PADWA"),
        ("MAKARSANKRANTI", "MAKARSANKRANTI"),
        ("CHRISTMAS DAY", "CHRISTMAS DAY"),
        ("QUIZ", "QUIZ"),
        ("GROUP PERFORMANCE", "GROUP PERFORMANCE"),
        ("SPEECH", "SPEECH"),
        ("INDEPENDENCE DAY", "INDEPENDENCE DAY"),
        ("REPUBLIC DAY", "REPUBLIC DAY"),
        ("NEW YEAR PARTY", "NEW YEAR PARTY"),
        ("SINGING", "SINGING"),
        ("DANCING", "DANCING"),
        ("WEDDING", "WEDDING"),
        ("ENGAGEMENT", "ENGAGEMENT"),
        ("Information Sharing", "Information Sharing"),
        ("Decision making", "Decision making"),
        ("Brainstorming", "Brainstorming"),
        ("Training", "Training"),
        ("Innovation", "Innovation"),
        ("Management", "Management"),
    )

    ename = models.CharField(max_length=30, choices=ENAME_CHOICES, default="SINGING")
    Contact = models.CharField(max_length=11)
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    )
    Gender = models.CharField(max_length=9,
                              choices=GENDER_CHOICES,
                              default="MALE")

    # Eventcategory = models.CharField(max_length=30)
    # Eventname = models.CharField(max_length=30)

    class Meta:
        db_table = "eventreg"


class Meetingreg(models.Model):
    objects = None
    VENUEM_CHOICES = (
        ("Information Sharing", "Information Sharing"),
        ("Decision making", "Decision making"),
        ("Brainstorming", "Brainstorming"),
        ("Training", "Training"),
        ("Innovation", "Innovation"),
        ("Management", "Management"),
    )
    meetingname = models.CharField(max_length=20,
                                   choices=VENUEM_CHOICES,
                                   default="Decision making")

    meetinghead = models.CharField(max_length=30)
    meetingheadmob = models.CharField(max_length=10)
    VENUE_CHOICES = (
        ("NASHIK", "NASHIK"),
        ("MUMBAI", "MUMBAI"),
        ("PUNE", "PUNE"),
        ("THANE", "THANE"),
        ("DADAR", "DADAR"),
        ("SURAT", "SURAT"),
    )
    meetingvenue = models.CharField(max_length=20,
                                    choices=VENUE_CHOICES,
                                    default="NASHIK")

    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    totalmembers = models.IntegerField(10)
    GENDER_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    meetingduration = models.CharField(max_length=30, choices=GENDER_CHOICES, default=1)
    END_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    meetinghallno = models.CharField(max_length=30, choices=END_CHOICES, default=1)

    class Meta:
        db_table = "meetingtable"


class Exhibitionreg(models.Model):
    objects = None
    cname = models.CharField(max_length=30)
    cadd = models.CharField(max_length=30)
    ENDER_CHOICES = (
        ("NASHIK", "NASHIK"),
        ("MUMBAI", "MUMBAI"),
        ("PUNE", "PUNE"),
        ("THANE", "THANE"),
        ("DADAR", "DADAR"),
        ("SURAT", "SURAT"),
    )
    ccity = models.CharField(max_length=20,
                             choices=ENDER_CHOICES,
                             default="NASHIK")
    G_CHOICES = (
        ("MAHARASHTRA", "MAHARASHTRA"),
        ("GUJRAT", "GUJRAT"),
        ("MADHYA PRADESH", "MADHYA PRADESH"),
        ("TAMILNADU", "TAMILNADU"),
        ("RAJASTHAN", "RAJASTHAN"),
        ("HARIYANA", "HARIYANA"),
    )
    cstate = models.CharField(max_length=20,
                              choices=G_CHOICES,
                              default="MAHARASHTRA")
    date = models.DateField()
    time = models.TimeField()
    ctel = models.CharField(max_length=11)
    GE_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    duration = models.CharField(max_length=30, choices=GE_CHOICES,
                                default="1")

    class Meta:
        db_table = "exhibitiontable"


class Festivalreg(models.Model):
    objects = None
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    contact = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    GEN_CHOICES = (
        ("DIWALI", "DIWALI"),
        ("GUDHI PADWA", "GUDHI PADWA"),
        ("MAKARSANKRANTI", "MAKARSANKRANTI"),
        ("CHRISTMAS DAY", "CHRISTMAS DAY"),
    )
    festtheme = models.CharField(max_length=20,
                                 choices=GEN_CHOICES,
                                 default="DIWALI")

    date = models.DateField()
    GENDERR_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    duration = models.CharField(max_length=30, choices=GENDERR_CHOICES,
                                default="1")
    themedesc = models.CharField(max_length=100)

    class Meta:
        db_table = "festivaltable"


class Culturalreg(models.Model):
    objects = None
    GENDER_CHOICES = (
        ("QUIZ", "QUIZ"),
        ("GROUP PERFORMANCE", "GROUP PERFORMANCE"),
        ("SPEECH", "SPEECH"),
        ("INDEPENDENCE DAY", "INDEPENDENCE DAY"),
        ("REPUBLIC DAY", "REPUBLIC DAY"),
    )
    ename = models.CharField(max_length=20,
                             choices=GENDER_CHOICES,
                             default="QUIZ")
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    date = models.DateField()
    GENDE_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    duration = models.CharField(max_length=30, choices=GENDE_CHOICES,
                                default="1")
    total = models.CharField(max_length=100)

    class Meta:
        db_table = "culturaltable"


class Entertainmentreg(models.Model):
    objects = None
    ENT_CHOICES = (
        ("NEW YEAR PARTY", "NEW YEAR PARTY"),
        ("SINGING", "SINGING"),
        ("DANCING", "DANCING"),
        ("WEDDING", "WEDDING"),
        ("ENGAGEMENT", "ENGAGEMENT"),
    )
    ename = models.CharField(max_length=20,
                             choices=ENT_CHOICES,
                             default="SINGING")
    contact = models.CharField(max_length=10, unique=True)
    eholdername = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    evenue = models.CharField(max_length=30)
    date = models.DateField()
    ticket = models.FloatField()
    DURAT_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    duration = models.CharField(max_length=30, choices=DURAT_CHOICES,
                                default="1")
    total = models.CharField(max_length=100)

    class Meta:
        db_table = "entertainmenttable"


class Hospitalityreg(models.Model):
    objects = None
    GEND_CHOICES = (
        ("NEW YEAR PARTY", "NEW YEAR PARTY"),
        ("SINGING", "SINGING"),
        ("DANCING", "DANCING"),
        ("WEDDING", "WEDDING"),
        ("ENGAGEMENT", "ENGAGEMENT"),
    )
    ename = models.CharField(max_length=20,
                             choices=GEND_CHOICES,
                             default="SINGING")

    eholdername = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    FOODTYPE_CHOICES = (
        ("VEG", "VEG"),
        ("NON-VEG", "NON-VEG"),
    )
    foodtype = models.CharField(max_length=20,
                                choices=FOODTYPE_CHOICES,
                                default="VEG")
    FOODNAME_CHOICES = (
        ("AALOO MATAR", "AALOO MATAR"),
        ("MANCHURIAN", "MANCHURIAN"),
        ("PARATHA", "PARATHA"),
        ("SABUDANA VADA", "SABUDANA VADA"),
        ("KHICHDI", "KHICHDI"),
    )
    foodname = models.CharField(max_length=20,
                                choices=FOODNAME_CHOICES,
                                default="MANCHURIAN")
    evenue = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    DURATI_CHOICES = (
        ("1 day", '1'),
        ("2 days", '2'),
        ("3 days", '3'),
        ("4 days", '4'),
        ("5 days", '5'),
        ("6 days", '6'),
        ("7 days", '7'),
        ("8 days", '8'),
        ("9 days", '9'),
        ("10 days", '10'),
        ("11 days", '11'),
    )
    duration = models.CharField(max_length=30, choices=DURATI_CHOICES,
                                default="1")
    total = models.CharField(max_length=100)

    class Meta:
        db_table = "hospitalitytable"
