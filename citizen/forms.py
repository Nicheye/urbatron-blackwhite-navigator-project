from django import forms
from .models import CitReport
class Citizen_report(forms.ModelForm):
	class Meta:
		model = CitReport
		fields = ('type_of_problem','title','description',
		)		
		widgets = {
			'type_of_problem':forms.Select(attrs={
				"class":"form-select form-select-lg mb-3",
				"required":"true",
			}),
			'title':forms.TextInput(attrs={
				"type":"tel",
				"class":"form-control",
				"name:":"",
				"placeholder":"название",
				"required":"true",
				
			}),
			'description':forms.Textarea(attrs={
				
				"class":"form-control citizen_rep_area",
				"name:":"",
				"id":"exampleFormControlTextarea1",
				"placeholder":"описание",
				"required":"true",
				"rows":3
				
			}),
		
		}
		