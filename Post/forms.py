from django import forms
from .models import Post
from flatpickr import DatePickerInput
from django.forms.widgets import CheckboxSelectMultiple

class PostForm(forms.ModelForm):
   
    class Meta:
        model=Post
        fields=['title','subject','docnumber','duedate','content']

        widgets = {
            'duedate': DatePickerInput(),
            
            
        }


class UpdatePostForm(forms.ModelForm):
   
    class Meta:
        model=Post
        mail_group = forms.BooleanField(required=False)
        #fields=['title','subject','docnumber','duedate','content','status','mail_group']
        fields=['title','subject','docnumber','duedate','content','status','mail_group']
        widgets = {
            'duedate': DatePickerInput(),
            'mail_group':CheckboxSelectMultiple(),
            #'status':RadioSelect(),

        }

 

