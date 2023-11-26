from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Munic_works)
admin.site.register(Type_of_munic_works)
admin.site.register(Poll)
admin.site.register(Poll_Option)