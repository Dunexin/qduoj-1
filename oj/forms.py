#coding=utf8
from  django import forms

class Login(forms.Form):
	name = forms.CharField(label='用户')
	password = forms.CharField(label='密码', widget=forms.PasswordInput)

class Register(forms.Form):
	name = forms.CharField(label='用户名')
	password = forms.CharField(label='输入密码', widget=forms.PasswordInput)
	ensure_pw = forms.CharField(label='确认密码', widget=forms.PasswordInput)
	email = forms.EmailField(label='Email')
	website = forms.URLField(label='website', required=False)




