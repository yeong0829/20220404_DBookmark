from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts import models
from accounts.models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='사용자명', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '영어 소문자 대문자, 숫자만 가능, 특수문자, 공백 입력 안됨',
    }))
    nickname = forms.CharField(label='별명')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', ) #('username', 'email', )


    def save(self):
        user = super().save()
        new_profile = Profile.objects.create(
            user=user,
            nickname=self.cleaned_data.get('nickname')  #self.cleaned_data['nickname']
        )
        return new_profile


class LoginForm(models.ModelForm):
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
