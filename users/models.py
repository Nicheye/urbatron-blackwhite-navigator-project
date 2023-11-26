from django.db import models

# Create your models here.
from django.db import models
import gettext
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, role, email, second_name, father_name, bday ,first_name,phone_number, city ,password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(role, email, second_name, father_name, bday ,first_name,phone_number, city ,password, **other_fields)

    def create_user(self, role, email, second_name, father_name, bday ,first_name,phone_number, city ,password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        city1=City.objects.get(id=city)
        role1 = Role.objects.get(id=role)
        user = self.model(role=role1,email=email, second_name=second_name,
                          father_name=father_name,bday=bday,phone_number=phone_number,
                          city=city1,
                          first_name=first_name, **other_fields)
        other_fields.setdefault('is_active', True)
        user.set_password(password)
        user.save()
        return user
# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self):
        return self.title
class City(models.Model):
    title = models.CharField(max_length=25)
    def __str__(self):
        return self.title
    
class NewUser(AbstractBaseUser,PermissionsMixin):
    role = models.ForeignKey(Role,related_name="role",on_delete=models.CASCADE)
    email = models.EmailField(_('email address'),unique=True)
    first_name =  models.CharField(max_length=150)
    father_name =  models.CharField(max_length=150)
    second_name =  models.CharField(max_length=150)
    bday=models.DateField(auto_now=False, auto_now_add=False)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')],unique=True)
    city = models.ForeignKey(City,related_name="city",on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_proved = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','first_name',"second_name","role","father_name","bday","city"]
    def __str__(self):
        return self.phone_number
	 			
class CommonPost(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=70,default="Msc")
    content = models.CharField(blank=True,max_length=10000)
    image = models.ImageField(upload_to="common_posts")
    date = models.CharField(blank=True,max_length=10000,default="21.10.2023")
    time = models.CharField(blank=True,max_length=10000,default="23:05")
    link = models.CharField(blank=True,max_length=10000,default="https://google.com")
    date_create = models.DateField(auto_now_add=True)
    author = models.ForeignKey(NewUser,related_name="author_of_common_post",on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(CommonPost,related_name="comment_for_common_post",on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    author = models.ForeignKey(NewUser,related_name="commentator",on_delete=models.CASCADE)
class Profile(models.Model):
    Male = 'Male'
    Female = 'Female'
    GENDER_CHOICE = [
        (Male,'Мужчина'),
        (Female,'Женщина')
    ]
    Student = 'Student'
    Worker = 'Worker'
    Server = 'Server'
    Retired = 'Retired'
    Bus_CHOICE = [
        (Student,'Студент'),
        (Worker,'Рабочий'),
        (Server,'Служащий'),
        (Retired,'Пенисионер'),


    ]
    user = models.OneToOneField(NewUser,null=True,on_delete=models.CASCADE)
    bis = models.CharField(max_length=10,choices=Bus_CHOICE,default=Worker)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICE,default=Female)
    elo=  models.PositiveIntegerField(default=0)
    votes =  models.PositiveIntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    comments =  models.PositiveIntegerField(default=0)
    avatar = models.ImageField(upload_to="avatars",default="./static/images/blank_logo.png")			
class RecentNew(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=3309)
   
    created_at = models.DateTimeField(auto_now_add=True)
	