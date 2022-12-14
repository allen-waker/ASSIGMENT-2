"""
1.Why Django should be used for web-development? Explain how you
can create a project in Django? 

Ans.Django is the best framework for web applications, as it allows developers to use modules for faster development.
 As a developer, you can make use of these modules to create apps, websites from an existing source.
 It speeds up the development process greatly, as you do not have to code everything from scratch.
print("------------------------------!--------------------------------------------------------")
2.How to check installed version of django? 

Ans.Simply type python -m django --version or type pip freeze to see all the versions of installed modules including Django.
print("------------------------------!--------------------------------------------------------")

3.Explain what does django-admin.py make messages command is used
  for?

Ans. Runs over the entire source tree of the current directory and pulls out all strings marked for translation.
 It creates (or updates) a message file in the conf/locale (in the Django tree) or locale (for project and application) directory.
print("------------------------------!--------------------------------------------------------")

4.What is Django URLs?make program to create django urls

Ans.Django is a web application framework, it gets user requests by URL locater and responds back. To handle URL, django.urls module is used by the framework.

    //urls.py

    from django.contrib import admin  
from django.urls import path  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
] 
print("------------------------------!--------------------------------------------------------")

5.What is a QuerySet?Write program to create a new Post object in
database: 

Ans.Django ORM is one of the best tools of Django and plays very essential role to perform database related tasks.
 It provides abstractions with the database, in a mostly database agnostic way.

 ORM consists of ease of use abstraction. It keeps "Simple things easy and hard things possible."

 from django.http import HttpResponse
from django.template import loader
from .models import Members

def testing(request):
  mydata = Members.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }

 return HttpResponse(template.render(context, request))
print("------------------------------!--------------------------------------------------------")
 6.Explain what does django-admin.py make messages command is used
for?

Ans.django-admin makemessages¶
Runs over the entire source tree of the current directory and pulls out all strings marked for translation.
 It creates (or updates) a message file in the conf/locale (in the Django tree) or locale (for project and application) directory.

 After making changes to the messages files you need to compile them with compilemessages for use with the builtin gettext support.
print("------------------------------!--------------------------------------------------------")
7.Mention what command line can be used to load data into Django?


Ans.To load data into Django you have to use the command line Django-admin.py loaddata.
 The command line will searches the data and loads the contents of the named fixtures into the data.
 """