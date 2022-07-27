from urllib.request import Request
from wsgiref.util import request_uri
from django.shortcuts import render
from .models import Foundation
from .forms import FoundationForm, RawFoundationForm
# Create your views here.


#def foundation_create_view(request):
    #my_form = RawFoundationForm()
    #if request.method == "POST":
        #my_form = RawFoundationForm(request.POST)
        #if my_form.is_valid():
       #     Foundation.objects.create(**my_form.cleaned_data)
      #  else:
     #       print(my_form.error)
    #my_form = RawFoundationForm()
    #context = {
      #  "form": my_form
    #    }
   # return render(request, "foundation/foundation_create.html",context)


def foundation_create_view(request):
    form = FoundationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FoundationForm()
        
    context ={
        'form': form
    }
    return render(request,"foundation/foundation_create.html",context)


def foundation_detail_view(request):
    obj = Foundation.objects.get(id=1)
   # context = {
   #     'title': obj.Foundation_Name, 
   #     'focus': obj.Focus_area,
   #     'adress':obj.Address,
   #     'email':obj.Email,
   #     'phone':obj.Phone,
   #     'website':obj.Website,

    #}

    context ={
        'object': obj

    }
    return render(request,"foundation/foundation_detail.html",context)