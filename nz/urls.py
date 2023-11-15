from nz.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('williamson/',williamson,name='williamson'),
    path('philips/',philips,name='philips'),
]