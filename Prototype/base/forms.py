from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class UseForm(UserCreationForm):
    email = forms.EmailField(label='email')
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'group')
