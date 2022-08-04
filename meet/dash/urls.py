from . import views
from django.urls import path

app_name = 'dash'

urlpatterns =[
    path('create_meet/', views.create_meet, name='create_meet'),
    path('authorize/', views.authorize, name = 'authorization')
]