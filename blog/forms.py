from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Post ,Category
from django.contrib.auth.models import User  #built in user model


class contactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject  = forms.CharField(required=True)
    message= forms.CharField(widget=forms.Textarea,required=True)

choices = Category.objects.all().values_list("name","name") #to make it dynamic if we add category vlaue in our admin model panel


"""below is the method of hard coding without it being dynamic"""

choice_list= []

for item in choices:
    choice_list.append(item)

# choices = [("Devices","Devices"),
# ("Coding Bootcamp in SA","Coding Bootcamp in SA"),
# ("Online Platforms","Online Platforms"),("Tools","Tools"),
# ("Web Development","Web Development"),("Data Science","Data Science"),
# ("Programming Languages","Programming Languages"),
# ("Applications","Applications"),("Software","Software")] 
#we are making a selct box oand they have to be double


class PostForm(forms.ModelForm):
    


    class Meta:
        model =Post
        fields =("title","author","topic_category","content")

        widgets = {
            # "title":forms.TextInput(attrs={"class":"form-control","placeholder":"this is tile placeholder stuff"}),

            "title":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.Select(attrs={"class":"form-control"}),
            # "topic_category":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "topic_category":forms.Select(choices=choice_list,attrs={"class":"form-control"}),
                #choices go first before attrs




        }




class EditForm(forms.ModelForm):
    class Meta:
         model =Post
         fields =("title","topic_category","content")
         widgets = {
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"this is tile placeholder stuff"}),

            "title":forms.TextInput(attrs={"class":"form-control"}),
            # "author":forms.Select(attrs={"class":"form-control"}),
            "topic_category":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}), }
        