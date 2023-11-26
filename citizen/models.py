from django.db import models
from users.models import City,NewUser

class ReportStatus(models.Model):
	title = models.CharField(max_length=10)
	def __str__(self) :
		return self.title
class ReportProblems(models.Model):
	title = models.CharField(max_length=20)
	def __str__(self) :
		return self.title
# Create your models here.
class CitReport(models.Model):
	type_of_problem = models.ForeignKey(ReportProblems,related_name="type_of_problem",on_delete=models.CASCADE)
	status = models.ForeignKey(ReportStatus,related_name="cit_report_status",on_delete=models.CASCADE)
	title = models.CharField(max_length=80)
	description = models.CharField(max_length=500,blank=True)
	city=models.ForeignKey(City,related_name="city_of_citizen_report",on_delete=models.CASCADE,default=1)
	comment = models.CharField(max_length=1000,blank=True,default=None)
	react= models.CharField(default=None,null=True,blank=True,max_length=1000)
	created_by = models.ForeignKey(NewUser,related_name="author_of_cit_report",on_delete=models.CASCADE,default=1)

