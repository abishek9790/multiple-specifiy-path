from django.urls import path
from app1.views import *
app1='something2'
urlpatterns=[
    path('funa/',funa,name='funa'),
    path('funb/',funb,name='funb'),
]
