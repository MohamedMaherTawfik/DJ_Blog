from django import forms
from .models import post



class postform(forms.ModelForm):
    class Meta:
        model=post
        #fields='__all__'
        fields=['title','content','image','tags']

