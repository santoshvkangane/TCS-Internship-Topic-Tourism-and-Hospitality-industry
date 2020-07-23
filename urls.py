
from django.contrib import admin
from django.urls import path
from django.urls import path
from tourismapp import views
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from tourismhospitality import settings

urlpatterns = [
    path('mainpage', views.main),
     path('users', views.Users),
    path('signup', views.signup),
    path('signin', views.signin),
    path('admin', views.adminlogin),
    path('Hmpage', views.Homepage),
    # path('eventmanager', views.Eventmanager),
    path('eventregister', views.Eventregister),
    path('eventregtable', views.Eventregtable),
    path('eventadvertisement', views.Eventadvertisement),
    path('eventorganize', views.Eventorganize),
    path('eventattendee', views.Eventattendee),
    path('eventmarketing', views.Eventmarketing),
    path('eventticketing', views.Eventticketing),
    path('eventmonitoring', views.Eventmonitoring),
    path('eventbooking', views.Eventbooking),
    path('payment', views.Payment),
    path('finalpmt', views.Payment),
    path('meeting', views.Meeting),
    path('meetingtable', views.Meetingtable),
    path('exhibition', views.Exhibition),
    path('exhibitiontable', views.Exhibitiontable),
    path('festival', views.Festival),
    path('festivaltable', views.Festivaltable),
    path('cultural', views.Cultural),
    path('culturaltable', views.Culturaltable),
    path('entertainment', views.Entertainment),
    path('entertainmenttable', views.Entertainmenttable),
    path('hospitality', views.Hospitality),
    path('hospitalitytable', views.Hospitalitytable),
    path('article', views.Article),
    path('contact', views.Contact),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)