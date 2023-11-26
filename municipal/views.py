from django.shortcuts import render,redirect
from .forms import Munic_work
from citizen.models import CitReport
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_post(request):
	role = str(request.user.role)
	if role =='Municipal':
		if request.method =='POST':
			form =Munic_work(request.POST,request.FILES)
			if form.is_valid():
				f = form.save(commit=False)
				f.author = request.user
				f.city = request.user.city
				
				f.save()
				return redirect('events')
				# username = form.cleaned_data['phone_number']
				# password = form.cleaned_data['password1']
				# user = authenticate(username=username,password=password)
				# login(request,user)
				

		else:
			form = Munic_work()
		return render(request,'create_munic_work.html',{"form":form})
	else:
		return redirect('home')
@login_required	
def check_reports(request):
	
	role =str(request.user.role)
	if role =='Municipal':
		reports = CitReport.objects.filter(city=request.user.city,comment="")
		
		print(reports)
		return render(request,'check_reports.html',{"reports":reports,"role":role})
	else:
		return redirect('home')

