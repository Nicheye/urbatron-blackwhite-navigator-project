from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CitReport)
admin.site.register(ReportProblems)
admin.site.register(ReportStatus)