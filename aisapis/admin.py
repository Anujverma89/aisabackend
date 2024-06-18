from django.contrib import admin
from .models import feedBackModel,faqs,Blog,events,members,gallery,joinAisa,notice,author,blogImage
# Register your models here.
modellist = [feedBackModel,faqs,Blog,events,members,gallery,joinAisa,notice,author,blogImage]

admin.site.register(modellist)