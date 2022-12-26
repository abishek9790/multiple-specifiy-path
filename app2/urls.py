from django.urls import path
from app2.views import *
app2='something3'
urlpatterns=[
    path('func/',func,name='func'),
    path('fund/',fund,name='fund'),
]