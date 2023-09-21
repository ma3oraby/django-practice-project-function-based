from django import forms
from .models   import Login

class LoginForm (forms.ModelForm) :
    class Meta :
        model = Login  
        fields = '__all__'

# class LoginForm (forms.Form) :
#     username = forms.CharField(max_length=50,label='name',initial='enter username',disabled=True)
#     password = forms.CharField(max_length=50,widget=forms.PasswordInput,label='passcode',initial='enter password',help_text='at least 8 characters',required=True)