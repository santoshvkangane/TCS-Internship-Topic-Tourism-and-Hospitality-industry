from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
###################################################33
def main(request):
    return render(request, 'mainpage.html')


################################################
def signup(request):
    if request.method == "POST":
        form = Signup2Form(request.POST)
        print(form)
        password = request.POST['password']
        password2 = request.POST['password2']
        if form.is_valid() and password == password2:
            form.save()
            return redirect("/signin")
        else:
            form = "Password does not Matched"
            return render(request, "sign_up.html", {'form': form})
    else:
        print("attach else")
        form = Signup2Form()
        return render(request, "sign_up.html", {'form': form})


#####################################

def signin(request):
    print("in sign in!!!!!!")
    # Output message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == "POST":
        # Create variables for easy access
        print("in if condition!!!!!!")
        username = request.POST['username']
        password = request.POST['password']
        user = Signup2.objects.all()
        # Check if account exists using MySQL

        for i in user:
            if username == 'admin' and password == 'admin':
                msg = Signup2.objects.all()
                m = 0
                for users in msg:
                    print("for loop")
                    m = m + 1
                return redirect('/admin')

            elif i.username == username and i.password == password:
                print("for login!!!!!!")
                msg = i.username
                user = 1
                break
        if user == 1:
            return render(request, "Hmpage.html", {'msg1': msg})

        else:
            # msg = 'Please Fill Proper fields'
            return render(request, "sign_in.html", {'msg2': "Wrong USERNAME or PASSWORD..."})

    else:
        print("in else loop two11!!!!!!!!")
        # msg = 'Please Fill Proper fields'
        return render(request, "sign_in.html")


#########################

def adminlogin(request):
    msg = Signup2.objects.all()
    m = 0
    for users in msg:
        print("for loop")
        m = m + 1
    return render(request, "admin.html", {'m': m})


def Users(request):
    home = Signup2.objects.all()
    return render(request, "users.html", {'home': home})


####################
def Homepage(request):
    return render(request, "Hmpage.html")


###############

def Eventmanager(request):
    return render(request, 'eventmanager.html')


#####################
def render_to_response(param):
    pass


def Eventregister(request):
    if request.method == 'POST':
        form = EventregForm(request.POST)
        print(form.errors)
        fname = request.POST.get('Firstname')
        lname = request.POST.get('Lastname')
        email = request.POST.get('EmailId')
        event = request.POST.get('ename')
        cont = request.POST.get('Contact')
        gender = request.POST.get('Gender')
        eventfees = 100
        totalamt = 100

        if form.is_valid():
            form.save()
            print("in if part")
            return render(request, 'payment.html',
                          {'fname': fname, 'lname': lname, 'email': email, 'event': event, 'cont': cont,
                           'gender': gender, 'eventfees': eventfees, 'totalamt': totalamt})
        else:
            return HttpResponse('Contact or Email has been used already')
    else:
        print("in else part")
        form = EventregForm()
        return render(request, 'eventregister.html', {'form': form})


def Eventregtable(request):
    home = Eventreg.objects.all()
    return render(request, "eventregtable.html", {'home': home})


def Payment(request):
    # user = Signup2.objects.get('username')
    return redirect('/Hmpage')


#######################
def Eventadvertisement(request):
    return render(request, 'eventadvertisement.html')


#################

def Eventorganize(request):
    return render(request, 'eventorganize.html')


def Meeting(request):
    if request.method == 'POST':
        meet = MeetingregForm(request.POST)
        print(meet.errors)
        if meet.is_valid():
            meet.save()
            return redirect('/meetingtable')

    else:
        meet = MeetingregForm()
        return render(request, "meeting.html", {'meet': meet})


def Meetingtable(request):
    home = Meetingreg.objects.all()
    return render(request, "meetingtable.html", {'home': home})


def Exhibition(request):
    if request.method == 'POST':
        meet = ExhibitionregForm(request.POST)
        print(meet)
        if meet.is_valid():
            meet.save()
            return redirect('/exhibitiontable')
        else:
            return HttpResponse('invalid credentials')

    else:
        meet = ExhibitionregForm()
        return render(request, "exhibition.html", {'meet': meet})


def Exhibitiontable(request):
    home1 = Exhibitionreg.objects.all()
    return render(request, "exhibitiontable.html", {'home1': home1})


def Festival(request):
    if request.method == 'POST':
        meet = FestivalregForm(request.POST)
        print(meet.errors)
        if meet.is_valid():
            meet.save()
            return redirect('/festivaltable')

    else:
        meet = FestivalregForm()
        return render(request, "festival.html", {'meet': meet})


def Festivaltable(request):
    home = Festivalreg.objects.all()
    return render(request, "festivaltable.html", {'home': home})


def Cultural(request):
    if request.method == 'POST':
        meet = CulturalregForm(request.POST)
        print(meet.errors)
        if meet.is_valid():
            meet.save()
            return redirect('/culturaltable')

    else:
        meet = CulturalregForm()
        return render(request, "cultural.html", {'meet': meet})


def Culturaltable(request):
    home = Culturalreg.objects.all()
    return render(request, "culturaltable.html", {'home': home})


def Entertainment(request):
    if request.method == 'POST':
        meet = EntertainmentregForm(request.POST)
        print(meet.errors)
        if meet.is_valid():
            meet.save()
            return redirect('/entertainmenttable')

    else:
        meet = EntertainmentregForm()
        return render(request, "entertainment.html", {'meet': meet})


def Entertainmenttable(request):
    home = Entertainmentreg.objects.all()
    return render(request, "entertainmenttable.html", {'home': home})


def Hospitality(request):
    if request.method == 'POST':
        meet = HospitalityregForm(request.POST)
        print(meet.errors)
        if meet.is_valid():
            meet.save()
            return redirect('/hospitalitytable')

    else:
        meet = HospitalityregForm()
        return render(request, "hospitality.html", {'meet': meet})


def Hospitalitytable(request):
    home = Hospitalityreg.objects.all()
    return render(request, "hospitalitytable.html", {'home': home})


#########################

def Eventattendee(request):
    return render(request, 'eventattendee.html')


###################

def Eventmarketing(request):
    return render(request, 'eventmarketing.html')


#################

def Eventticketing(request):
    return render(request, 'eventticketing.html')


#########################

def Eventmonitoring(request):
    return render(request, 'eventmonitoring.html')


###################

def Eventbooking(request):
    return render(request, 'eventbooking.html')


#########################

def Article(request):
    return render(request, "article.html")


def Contact(request):
    return render(request, "contact.html")

###################
