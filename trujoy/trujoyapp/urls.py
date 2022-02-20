from django.conf.urls import url
from .import views


urlpatterns = [

    url('events/', views.eventslist, name="eventslist"),
    url('welcome/',views.welcome),
    url('registration/',views.index),
    url('user_home/',views.user_home),
    url('test/',views.test,name='test'),
    url('login_user/',views.login_user,name='login_user'),



    url('ground_booking/',views.ground_booking,name='ground_booking'),
    url('conform/',views.db_ground_booking,name='db_ground_booking'),
    url('payment/', views.payment, name='payment'),

    url('contact/', views.contact, name='contact'),

    url('totevents/', views.eventsss, name='eventss'),
    url('eventsbooked/', views.main_view, name='eventsbooked'),

    url('user_logout/',views.user_logout,name='user_logout'),
    url('dashboard/', views.dashboard),



]
