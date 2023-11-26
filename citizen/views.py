from django.shortcuts import render,redirect
from .forms import Citizen_report
# Create your views here.
from .models import ReportStatus,CitReport
from municipal.models import Poll,Poll_Option,Vote
from users.models import Profile
from django.contrib.auth.decorators import login_required
@login_required
def user_report(request):
	if request.method =='POST':
		form =Citizen_report(request.POST,request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.status = ReportStatus.objects.get(id=1)
			f.city = request.user.city
			f.comment = ""
			f.created_by = request.user
			f.save()
			profile = Profile.objects.get(user=request.user)
			profile.reports +=1
			profile.elo +=10
			profile.save()
			
			return redirect('profile',request.user.id)
			# username = form.cleaned_data['phone_number']
			# password = form.cleaned_data['password1']
			# user = authenticate(username=username,password=password)
			# login(request,user)
			

	else:
		form = Citizen_report()
	return render(request,'citizen_report_create.html',{"form":form})

def polls(request):
	polls = Poll.objects.filter(city=request.user.city,is_finished=False)

	
	return render(request,'polls.html',{"polls":polls})
@login_required
def poll_detail(request,id):
	

	poll =Poll.objects.get(id=id)
	options = Poll_Option.objects.filter(poll=poll)
	votes =Vote.objects.filter(poll=poll).count()
	
	if request.method =='POST':
		try:
			voted = Vote.objects.get(poll=poll,user=request.user)
			voted=True
			return render(request,'poll_detail.html',{"options":options,"poll":poll,"votes":votes,"voted":voted})
		except:
			
			id = request.POST.get('poll')
			option = Poll_Option.objects.get(id=id)
			option.count+=1
			option.save()
			v = Vote()
			v.user = request.user
			v.poll = poll
			v.save()
			profile = Profile.objects.get(user=request.user)
			profile.votes +=1
			profile.elo +=30
			profile.save()
			
	try:
		voted = Vote.objects.get(poll=poll,user=request.user)
		voted=True
		return render(request,'poll_detail.html',{"options":options,"poll":poll,"votes":votes,"voted":voted})
	except:
		voted=False
		return render(request,'poll_detail.html',{"options":options,"poll":poll,"votes":votes,"voted":voted})
@login_required
def citizen_report_detail(request,id):
	report = CitReport.objects.get(id=id)
	role =str(request.user.role)
	if request.method =='POST':
		comment = request.POST.get('comment')
		report.comment = comment
		report.status = ReportStatus.objects.get(id=2)
		report.save()
		return redirect('check_reports')
	return render(request,'citizen_report_detail.html',{"report":report,"role":role})
@login_required
def create_react(request,id):
	report =CitReport.objects.get(id=id)
	if  request.method =='POST':
		react = request.POST.get('react')
		report.react = react
		report.save()
		return redirect('citizen_report_detail',report.id)

def municipal_services(request):
	return render(request,'municipal_services.html')