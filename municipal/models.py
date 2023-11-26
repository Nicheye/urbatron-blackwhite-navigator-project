from django.db import models
from users.models import NewUser
from users.models import City
# Create your models here.
class Type_of_munic_works(models.Model):
	title = models.CharField(max_length=20)
	color = models.CharField(max_length=12)
	def __str__(self):
         return self.title

class Munic_works(models.Model):
		type = models.ForeignKey(Type_of_munic_works,related_name="type_of_municip_works",on_delete=models.CASCADE)
		title = models.CharField(max_length=50)
		description = models.CharField(max_length=1000)
		date_create = models.DateField(auto_now_add=True)
		dead_line_date = models.DateField(auto_now=False)
		city=models.ForeignKey(City,related_name="city_of_munic_works",on_delete=models.CASCADE,default=1)
		opt_image = models.ImageField(upload_to="munic_works_schedule_photos",blank=True,default="123.png")
		author = models.ForeignKey(NewUser,related_name="munic_work_creater",on_delete=models.CASCADE)
		def __str__(self):
			return self.title
		

class Poll(models.Model):
	title = models.CharField(max_length=150)
	city=models.ForeignKey(City,related_name="city_of_poll",on_delete=models.CASCADE,default=1)
	is_finished = models.BooleanField(default=False)
	start_time = models.DateField(auto_now_add=True)
	image = models.ImageField(upload_to="polls_images",default='')
	logo = models.ImageField(upload_to="polls_images",default='')
	
	winner=models.CharField(max_length=30,blank=True,default=" ")
	def __str__(self):
			return self.title


class Poll_Option(models.Model):
	title = models.CharField(max_length=150)
	poll = models.ForeignKey(Poll,related_name="poll_option",on_delete=models.CASCADE)
	count = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title
class Vote(models.Model):
	poll = models.ForeignKey(Poll,related_name="poll_for_vote",on_delete=models.CASCADE)
	user = models.ForeignKey(NewUser,related_name="voter_in_poll",on_delete=models.CASCADE)
		 
		 