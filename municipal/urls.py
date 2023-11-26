from django.db import models

# Create your models here.
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('create/',create_post,name="create_munic_work"),
   path('check_reports/',check_reports,name="check_reports")
]