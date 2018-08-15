from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

ROLE_CHOICES = (('LAWYER', 'Lawyer'),('GUEST', 'Guest'))

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email= forms.EmailField(help_text='Required.',required=True)
    password1 = forms.CharField(label=("Password"), 
    			widget=forms.PasswordInput,
    			help_text='Your password cannot be too similar to your other personal information.Your password must contain at least 8 characters.')
    role= forms.CharField(label='Signing in as A LAWYER or Guest', widget=forms.Select(choices=ROLE_CHOICES))
    bio=forms.CharField(label="Your Bio")
    location=forms.CharField(label="Your Location")



    def save(self,commit=True):
        user=super(SignUpForm,self).save(commit=False)
        user._role=self.cleaned_data['role']
        user._bio = self.cleaned_data['bio']
        user._location = self.cleaned_data['location']
        user._birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email','birth_date', 'password1', 'password2','role')



# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio', 'location', 'role')