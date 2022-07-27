from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view (request, *args, **kwargs):
    #print(request.user)
    #return HttpResponse ("<h1>Love code</>")
    return render(request, "home.html",{})


#def navbar (request, *args, **kwargs):
 #   return render (request,"navbar.html",{})


def contact (request,*args, **kwargs):
    return render (request,"contact.html",{})


def what_we_do (request,*args, **kwargs):
    my_context ={
        "my_location":"you are here",
        "my_list": [123, 111,321,'A']
    }

    return render (request,"what we do.html",my_context)


def about (request, *args, **kwargs):
    return render (request,"about.html",{})
