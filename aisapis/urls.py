from django.urls import path
from . import views


urlpatterns =[
    path("",views.home, name="home"),
    path("feedback",views.feedback, name="feedback"), #done
    path("members",views.fetchMembers,name="members"),
    path("notices",views.shownotices,name="shownotices"),
    path("joinaisa",views.joinAisavView,name="joinaisa"), #done
    path("galleryimages",views.galleryImages,name="galleryimages"),
    path("getfaqs",views.getFaqs,name="getfaqs"), #done
    path("getevents",views.getEvents,name="getevents"),
    path("getblogs",views.showBlog,name="showblog"), #done
]