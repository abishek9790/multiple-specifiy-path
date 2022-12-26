from django.urls import path
from app3.views import *
app3='something6'
urlpatterns=[
    path('fune/',fune,name='fune'),
    path('funf/',funf,name='funf'),
]