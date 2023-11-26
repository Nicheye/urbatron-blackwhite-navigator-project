from django.db import models

# Create your models here.
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   path('create/',user_report,name="create_citizen_report"),
   path('polls/',polls,name="citizen_polls"),
   path('poll/<int:id>/',poll_detail,name="poll_detail"),
   path('report/<int:id>',citizen_report_detail,name="citizen_report_detail"),
   path('create_react/<int:id>',create_react,name="create_react"),
   path('municipal_services/',municipal_services,name="municipal_services")
]