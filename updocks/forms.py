from django import forms
from .models import Post, Feed, FeedFile,PostFile
from django.forms import ModelForm, ModelChoiceField
from django.forms import ClearableFileInput
from django.forms import ClearableFileInput
...

class DateInput(forms.DateInput):
    input_type = 'date'


# class PostAddFrom(forms.ModelForm):#Для листвайв
#     class Meta:
#         model = Post
#         fields = ['title', 'data_add', 'date_end', 'cover', 'author']
#         widgets = {
#             'data_add': DateInput,
#             'date_end': DateInput,
#
#         }
class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'data_add', 'date_end', 'author', 'status', ]

class AddFormFile(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }




class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'data_add', 'date_end', 'author', 'cover' ,'more', 'status', ]
        widgets = {
            'data_add': DateInput,
            'date_end': DateInput,
            'cover': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        exclude = ('author',)



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class FeedModelForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['text']

class FileModelForm(forms.ModelForm):
    class Meta:
        model = FeedFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
        # widget is important to upload multiple files