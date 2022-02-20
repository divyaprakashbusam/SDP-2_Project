from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Sum
from .utils import get_plot



from .models import *

import datetime
from django.core.mail import send_mail


# Create your views here.
def welcome(request):
    return render(request,'index.html')

def eventslist(request):
    events = Events_list.objects.all()
    context={'events':events}
    return render(request, 'events.html', context)

#User Registration / Login Page
def index(request):
    return render(request,'registration.html')

#User Home Page
def user_home(request):
    if 'uname' in request.session:
        events = Events_list.objects.all()
        context = {'events': events}
        return render(request,'events.html',context)

    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',{"status":data})


#User Ground Booking Page
def ground_booking(request):
    if 'uname' in request.session:
        eventsobj=Events_list.objects.all()
        return render(request,'ground_booking.html',{"eventss":eventsobj})
    else:
        data = {'status':'You need to login first'}
        return render(request,'registration.html',context=data)

#User Logout
def user_logout(request):
    if 'uname' in request.session:
        del request.session['uname']

    if 'book_status' in request.session:
        del request.session['book_status']

    return render(request,'registration.html')



#BACKEND -> For User Registration
def test(request):
    register=False
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if(password == re_password):
            user = User(name=name,email=email,gender=gender,password=password)
            user.save()
            request.session['uname'] = name
            subject = 'THANKYOU FOR REGISTERING AT TRUJOY EVENTS'
            message = 'Hey '+user.name+',\n\nWe welcome you to the TruJoy Events Family!\n\n\n\n\nTruJoy Team'
            to = user.email
            send_mail(
                subject,
                message,
                'prakashbusam.dp999@gmail.com',
                [to],
            )
            register = True
            return user_home(request)
        else:
            data = {'status':"Password and Re-entered password must be same"}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For User Login
def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            user = User.objects.get(name=name)

            if user.password == password:
                request.session['uname'] = name
                return user_home(request)
            else:
                data = {'status':"Incorrect Password!!!"}
                return render(request,'registration.html',context=data)

        except Exception as e:
            data = {'status':"User does not exists! You have to register first."}
            return render(request,'registration.html',context=data)
    else:
        return HttpResponse("Something went wrong!!!!!")


#BACKEND -> For Ground Booking
def db_ground_booking(request):
    register = False
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        venue = request.POST.get('venue')
        people=request.POST.get('people')
        cat=request.POST.get('cat')
        name=request.POST.get('name')
        deco=request.POST.get('deco')
        price=request.POST.get('price')
        print(price)
        f=Events_list.objects.filter(name=price).distinct()
        print(f)
        li=[]

        for i in f:
            details={
                'name':i.name,
                'price':i.price

            }
            li.append(details)
        q = str(li[0]['price'])

        user = User.objects.get(name=request.session['uname'])
        book = Book_ground(uid=user.uid, name=user.name, mobile=mobile, email=email, date=date, time=time, venue=venue,
                           people=people, cat=cat, deco=deco, event=price, price=q)
        book.save()




        subject = 'BOOKING DETAILS'
        message = 'Hurray! your event is booked!!\n\nInorder to Proceed, Please Complete the Payment Process.\n\nYour Details are\n\nDate of the event: '+date+'\nTime of the event: '+time+'\nVenue of the event: '+venue+'\nNo.of People: '+people+'\nCatering: '+cat+'\nDecoration Theme: '+deco+'\nEvent: '+price+'\nTotal Amount: '+q+'\n\n\n\n\nTruJoy Team'
        to = user.email
        send_mail(
            subject,
            message,
            'prakashbusam.dp999@gmail.com',
            [to],
        )
        register = True
        request.session['book_status'] = "Booking successful"
        return render(request,'conform.html',{'date':date,'time':time,'venue':venue,'deco':deco,'name':user.name,'event':price,'people':people,'cat':cat,'price':q})

    return HttpResponse("Something went wrong!!")


def contact(request):
    if request.method == 'POST':
        con=Contact()
        name=request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        con.name=name
        con.email=email
        con.subject=subject
        con.save()
        return HttpResponse("<h1>Thanks For Contacting us</h1>")

    return render(request, 'contact.html')


def eventsss(request):
    return render(request, 'events-price.html')


def payment(request):
    return render(request,'payment.html')


def main_view(request):
    qs=Book_ground.objects.all()
    x=[x.event for x in qs]
    y=[y.price for y in qs ]
    chart=get_plot(x,y)
    return render(request,'eventsbooked.html', {'chart':chart})


def dashboard(request):
    return render(request, 'tableau.html')







