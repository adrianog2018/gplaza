from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
#from .models import UserProfile

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, unique=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('username')


"""
class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email')

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email')"""