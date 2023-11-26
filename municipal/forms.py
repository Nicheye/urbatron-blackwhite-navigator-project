from django import forms
from .models import Munic_works
class Munic_work(forms.ModelForm):
	class Meta:
		model = Munic_works
		fields = ('type','title','description','dead_line_date',
		'opt_image',)		
		widgets = {
			'type':forms.Select(attrs={
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
			'description':forms.TextInput(attrs={
				"type":"tel",
				"class":"form-control",
				"name:":"",
				"placeholder":"описание",
				"required":"true",
				
			}),
			'dead_line_date':forms.TextInput(attrs={
				"type":"date",
				"id":"date",
				"name:":"",
				"class":"form-control",
				"required":"true",
				
			}),
			'opt_image':forms.FileInput(attrs={

				"class":"form-control",
				
				
				"required":"true",
				
			}),
		}
		def form_valid(self, form):
			form.instance.author = self.request.user
			return super().form_valid(form)