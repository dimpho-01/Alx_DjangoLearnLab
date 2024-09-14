from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comment
from taggit.forms import TagWidget
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Form for updating profile information - assumes a profile model with bio and profile_picture fields
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, *args, **kwargs):
        # omit commit=False if using django-taggit
        instance = super(PostForm, self).save(commit=False)
        instance.save()
        if self.cleaned_data['tags']:
            instance.tags.set(*self.cleaned_data['tags'].split(','), clear=True)
        return instance