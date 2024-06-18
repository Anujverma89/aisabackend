from django.db import models

# Create your models here.

class feedBackModel(models.Model):
    name = models.CharField(max_length=100,null=False)
    college = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=150, null=False)
    who = models.CharField(max_length=100, null=False)
    feedback = models.TextField(max_length=1500, null=False)



class members(models.Model):
    branch={
        ("AIML","AIML"),
        ("AIDS","AIDS"),
    }
    year={
        ("SY","Second Year"),
        ("TY","Third Year"),
        ("Final","Final Year"),
    }
    post={
        ("p","president"),
        ("vp","Vice President"),
        ("secretary","Secretaries"),
        ("treasurer","Treasurers"),
        ("tech","Technical Team"),
        ("media","Media Team"),
        ("planning","Planning Team"),
        ("volunteers","Volunteers"),
        ("mentors","Mentors"),
    }
    name = models.CharField(max_length=100, null=False)
    post = models.CharField(max_length=100, null=False,choices=post)
    branch = models.CharField(max_length=100,null=False,choices=branch)
    year = models.CharField(max_length=200,null=False,choices=year)
    contact = models.CharField(max_length=10,null=False)
    image = models.ImageField(upload_to="member", null=False)
    

class joinAisa(models.Model):
    name = models.CharField(max_length=200,null=False)
    prn = models.CharField(max_length=10, null=False)
    department = models.CharField(max_length=50,null=False)
    contact = models.CharField(max_length=10,null=False)
    cgpa = models.CharField(max_length=5,null=False)
    type = models.CharField(max_length=100, null=False)

class faqs(models.Model):
    quesiton = models.TextField(null=False)
    answer = models.TextField(null=False)


class notice(models.Model):
    heading = models.CharField(max_length=200,null=False)
    url = models.URLField(null=False)
    description = models.TextField(null=False)
    image = models.FileField(upload_to="noticeboard",null=False)



# events and gallery related
class events(models.Model):
    eventchoises = {
        ("TE","Technical Events"),
        ("NTE", "Non Technical Events"),
        ("CDE","Carrier Development Events"),
    }
    eventName = models.CharField(max_length=100, null=False)
    eventDesc = models.TextField(null=False)
    eventImage = models.FileField(upload_to="events", null=False)
    eventType = models.CharField(max_length=200, choices=eventchoises,null=False)
    

class gallery(models.Model):
    eventName = models.ForeignKey(events,max_length=150,null=False,on_delete=models.CASCADE)
    galleryImage = models.FileField(upload_to="gallery", null=False)



# blog related information 
class author(models.Model):
    authorName = models.CharField(max_length=200,null=False)
    qualification = models.CharField(max_length=200, null=False)
    authorImage = models.FileField(upload_to="authorimage")

class Blog(models.Model):
    heading = models.CharField(max_length=200,null=False)
    decs = models.TextField(null=False)
    link = models.URLField()
    authorName = models.ForeignKey(author,on_delete=models.CASCADE)

class blogImage(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    image = models.FileField(upload_to="blogImage")



# join asia 

"""
Name
PRN
DEPT
Contact
CGPA
"""

"""
    Results table 


"""


"""
Update admin on any form update and changes in database

"""



#blogs
"""
Blogs section 

Heading
Title 
Author 
Content 
Published date 
Image 

"""

#resources 


#events 
"""
Event name 
Event image
Event catageory 
Event details 
"""

#gallary 

"""
image url :
Event name : events foreign key
Event type :  

"""

