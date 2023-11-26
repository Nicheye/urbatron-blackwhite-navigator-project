from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from .models import City,Role

class RegisterForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ("phone_number","first_name", "second_name","father_name", "bday", "email" , "city" , "role", "password1","password2")

		widgets= {
			'phone_number':forms.TextInput(attrs={
				"type":"tel",
				"class":"form-control",
				"name:":"",
				"placeholder":"Номер телефона",
				"required":"true",
				
			}),
			'first_name':forms.TextInput(attrs={
				"type":"text",
				"class":"form-control",
				"name:":"",
				"placeholder":"Номер телефона",
				"required":"true",
				
			}),
			'second_name':forms.TextInput(attrs={
				"type":"text",
				"class":"form-control",
				"name:":"",
				"placeholder":"Номер телефона",
				"required":"true",
				
			}),
			'father_name':forms.TextInput(attrs={
				"type":"text",
				"class":"form-control",
				"name:":"",
				"placeholder":"Номер телефона",
				"required":"true",
				
			}),
			'bday':forms.TextInput(attrs={
				"type":"date",
				"id":"date",
				"name:":"",
				"class":"form-control",
				"required":"true",
				
			}),
			'email':forms.TextInput(attrs={
				"type":"email",
				"class":"form-control",
				"name:":"",
				"placeholder":"email",
				"required":"true",
				
			}),
			'city':forms.Select(attrs={
				
				"class":"form-select form-select-lg mb-3",
							
				"required":"true",
				
			}),
			'role':forms.Select(attrs={
				
				"class":"form-select form-select-lg mb-3",
							
				"required":"true",
				
			}),
			'password1':forms.PasswordInput(attrs={
				
				"class":"form-control",
				"name:":"",
				"placeholder":"email",
				"required":"true",
				
			}),
			'password2':forms.PasswordInput(attrs={
				
				"class":"form-control",
				"name:":"",
				"placeholder":"email",
				"required":"true",
				
			}),
		}

