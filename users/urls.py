from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',views.home,name="home"),
   path('home',views.home,name="home"),
   path('sign-up',views.sign_up,name="sign_up"),
   path('profile/<int:id>',views.profile,name="profile"),
   path('posts',views.all_posts,name="all_posts"),
   path('create_post/',views.create_post,name="create_common_post"),
   path('post_detail/<int:id>/',views.post_detail,name="post_detail"),
   path('events/',views.events,name="events"),
   path('event/<int:id>/',views.event_detail,name="event_detail"),
   path('citizen_reports',views.citizen_reports,name="citizen_reports"),
   path('map/musorki',views.musorki,name="musorki"),
   path('map/eco',views.eco,name="eco"),
   path('map/roads',views.roads,name="roads"),
   path('maps',views.maps,name="maps"),
   path('leave_commment/<int:id>/',views.comment,name="comment"),
   path('awards/',views.award,name="awards"),
]
