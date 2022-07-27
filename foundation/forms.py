from xml.dom.minidom import Attr
from django import forms
from .models import Foundation

class FoundationForm (forms.ModelForm):
    Foundation_Name      = forms.CharField(widget = forms.TextInput(attrs={'class':"new-tite-class", "placeHolder":"Your foundation", 'max_length': 40}))
    Focus_area           = forms.CharField(required = False, 
                                           widget=forms.Textarea(attrs={
                                               "placeHolder":"Your focus area",
                                               'cols': 100
                                               }
                                                                 )
                                           )
    class Meta:
        model = Foundation
        fields = [
         'Foundation_Name',
            'Focus_area',
            'Address'
       ]


class RawFoundationForm(forms.Form):
    Foundation_Name      = forms.CharField(widget = forms.TextInput(attrs={'class':"new-tite-class", "placeHolder":"Your foundation", 'max_length': 40}))
    Focus_area           = forms.CharField(required = False, 
                                           widget=forms.Textarea(attrs={
                                               "placeHolder":"Your focus area",
                                               'cols': 100
                                               }
                                                                 )
                                           )
    Address              = forms.CharField()
    Email                = forms.EmailField()


        