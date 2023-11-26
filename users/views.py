from django.shortcuts import render

# Create your views here.
from citizen.models import CitReport
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import CommonPost,Profile
# Create your views here.
from .models import NewUser,RecentNew
from .forms import RegisterForm
from municipal.models import Munic_works
import time
from .models import Comment
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
def home(request):
		if request.user.is_authenticated:
			try:
				p = Profile.objects.get(user=request.user)
			except:
				p = Profile()
				p.user = request.user
				p.save()
			role = str(request.user.role)
		posts = CommonPost.objects.order_by('-id')[0:4]
		first_post = posts[0]
		second_post = posts[1]
		third_post = posts[2]
		fourth_post = posts[3]
		from .models import RecentNew
		
		last_recent = RecentNew.objects.order_by('-created_at').first()
		recent_news = RecentNew.objects.order_by('-created_at')
		if last_recent.created_at + datetime.timedelta(seconds=5)<timezone.now():

			import requests
			
			url = ('https://newsapi.org/v2/top-headlines?country=ru&apiKey=277f64c10a704e4da6b00bbe1ee26c36')

			response = requests.get(url)
			data = response.json()
			if recent_news.count()>=6:
				for recent_new in recent_news:
					recent_new.delete()
					
			articles = data['articles'][0:6]
			
			for article in articles:
				r = RecentNew()
				r.title = article['title']
				r.author = article['author']
				r.url = article['url']
				r.save()
		if request.user.is_authenticated:	
			return render(request,'main/home.html',{"role":role,"first_post":first_post,"second_post":second_post,"third_post":third_post,"fourth_post":fourth_post,"recent_news":recent_news})
		else:
			return render(request,'main/home.html',{"first_post":first_post,"second_post":second_post,"third_post":third_post,"fourth_post":fourth_post,"recent_news":recent_news})
	
def sign_up(request):
	if request.method =='POST':
		form =RegisterForm(request.POST)
		if form.is_valid():
			f =form.save(commit=False)
			f.is_active =True
			f.save()
			username = form.cleaned_data['phone_number']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('/')

	else:
		form = RegisterForm()
	return render(request,'registration/sign_up.html',{"form":form})
@login_required
def profile(request,id):
	user = NewUser.objects.get(id=id)
	role =str(user.role)
	profile = Profile.objects.get(user=user)
	if request.method =='POST':
		
		gender = request.POST.get('gender')
		
		
		bis = request.POST.get('bis')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		try:
			ava = request.FILES['ava_file']
			if ava is not None:
				profile.avatar = ava
				profile.save()
		except:
			pass
		print(phone,email)
		if gender is not None:
			profile.gender = gender
			profile.save()
		try:
			if bis !='':
				profile.bis = bis
				profile.save()
		except:
			pass
		if phone !='':
			user.phone_number = phone
		if email !='':
			user.email = email
		
		try:
			user.save()
		except:
			pass
		return redirect('profile',user.id)


	return render(request,'main/profile.html',{"user":user,"role":role})
@login_required
def citizen_reports(request):
	
	reports = CitReport.objects.filter(created_by=request.user).all()
	
	role =str(request.user.role)
	return render(request,'main/citizen_reports.html',{"reports":reports,"role":role})
def all_posts(request):
	posts = CommonPost.objects.all()
	return render(request,'main/all_posts.html',{"posts":posts})
@login_required			
def create_post(request):
	role =str(request.user.role)
	if request.method == 'POST' and role=='Municipal':
		post = CommonPost()
		post.title =request.POST.get('title')
		post.place =request.POST.get('place')
		post.content =request.POST.get('content')
		post.image =request.FILES['post_photo']
		post.date =request.POST.get('date')
		post.time =request.POST.get('time')
		post.link =request.POST.get('url')
		post.author = request.user
		post.save()
		return redirect('home')

	return render(request,'main/create_post.html',{"role":role})

def post_detail(request,id):
	get_post = CommonPost.objects.get(id=id)
	comments = Comment.objects.filter(post=get_post)
	return render(request,"main/common_posts_detail.html",{"post":get_post,"comments":comments})
@login_required	
def events(request):
	role = str(request.user.role)
	if  role =='Municipal':
		events =Munic_works.objects.filter(city = request.user.city).all()
		return render(request,"main/events.html",{"posts":events,"role":role})
	else:
		return redirect('home')
	

@login_required	
def event_detail(request,id):
	role = str(request.user.role)
	if  role =='Municipal':
		event =Munic_works.objects.get(id = id)
		event.opt_image
		return render(request,"main/event_detail.html",{"post":event})
	else:
		return redirect('home')
	
def musorki(request):
	return render(request,'maps/musorka.html',{})
def eco(request):
	return render(request,'maps/eco.html',{})
def roads(request):
	return render(request,'maps/eco.html',{})
def maps(request):
	from .models import City
	city = City.objects.all()
	return render(request,'maps/maps.html',{"citis":city})
@login_required
def comment(request,id):
	if request.method=='POST':
		post = CommonPost.objects.get(id=id)
		author = request.user
		comment =  request.POST.get('comment')
		
		c = Comment()
		c.post = post
		c.author = author
		c.comment = comment
		c.save()
		profile = Profile.objects.get(user=request.user)
		profile.comments +=1
		profile.elo +=20
		profile.save()
		return redirect('post_detail',post.id)
	
@login_required
def award(request):
	role = str(request.user.role)
	return render(request,'main/awards.html',{"role":role})