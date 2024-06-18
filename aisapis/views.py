from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import feedBackModel,members, notice, Blog, events, faqs, gallery, joinAisa
from .serializer import memeberSerializer,noticeSerializer, blogSerializer,faqSerializer,gallerySerializer,eventSerializer
from rest_framework.renderers import JSONRenderer
import json

# Create your views here.
def home(request):
    return HttpResponse("hello from homfaqse")

@csrf_exempt
def feedback(request):
    name = request.POST["name"]
    coll = request.POST["college"]
    dept = request.POST["dept"]
    wh = request.POST["who"]
    feed = request.POST["feedback"]
    # print(name, college,dept,who,feedback)
    feedBackModel.objects.create(name=name,college=coll, department=dept,who=wh, feedback= feed) 
    return JsonResponse({"res":"Feedback submitted","status":200})


def fetchMembers(request):
    member = members.objects.all()
    serializedata = memeberSerializer(member, many=True)
    data = JSONRenderer().render(serializedata.data)
    return HttpResponse(data,content_type='application/json')


def shownotices(request):
    notices = notice.objects.all()
    serealizedNotice = noticeSerializer(notices,many=True)
    data = JSONRenderer().render(serealizedNotice.data)
    return HttpResponse(data,content_type='application/json')


def showBlog(request):
    allblog = Blog.objects.all()
    serializedBlog = blogSerializer(allblog, many=True)
    data = JSONRenderer().render(serializedBlog.data)
    return HttpResponse(data,content_type="application/json")

def getEvents(request):
    allevents = events.objects.all()
    serializedEvent = eventSerializer(allevents,many=True)
    data = JSONRenderer().render(serializedEvent.data)
    return HttpResponse(data,content_type="application/json")

def getFaqs(request):
    allfaqs = faqs.objects.all()
    serializedFaqs = faqSerializer(allfaqs,many=True)
    data = JSONRenderer().render(serializedFaqs.data)
    return HttpResponse(data,content_type="application/json")

def galleryImages(request):
    allImages = gallery.objects.select_related('eventName')
    print(allImages.query)
    serializedgallery = gallerySerializer(allImages,many=True)
    print(serializedgallery)
    data = JSONRenderer().render(serializedgallery.data)
    return HttpResponse(data,content_type="application/json")

@csrf_exempt
def joinAisavView(request):
    if request.method == "POST":
        name = request.POST["name"]
        prn = request.POST["prn"]
        depart = request.POST["department"]
        contact = request.POST["contact"]
        gpa = request.POST["cgpa"]
        t=request.POST["type"]
        print(name,prn,depart,contact,gpa,t)
        enrollment = joinAisa(name=name,prn=prn,department= depart,contact=contact,cgpa=gpa,type=t)
        enrollment.save()
        return HttpResponse("Your request is saved", content_type="application/json")