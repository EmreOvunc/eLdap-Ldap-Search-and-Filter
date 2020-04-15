from django import forms


class SimpleForm(forms.Form):
    ldap_ip = forms.CharField(label='LDAP Server IP', max_length=100, widget=forms.TextInput(attrs={'size': 20, 'placeholder': '127.0.0.1'}))
    ldap_port = forms.CharField(label='LDAP Server Port', widget=forms.TextInput(attrs={'size': 5, 'placeholder': '389'}))
    search_base = forms.CharField(label='Search Base', max_length=100, widget=forms.TextInput(attrs={'size': 40, 'placeholder': 'dc=example,dc=com'}))
    search_filter = forms.CharField(label='Search Filter', max_length=100, widget=forms.TextInput(attrs={'size': 40, 'placeholder': 'cn=Alice'}))
    username = forms.CharField(label='Username', max_length=100, required=False, widget=forms.TextInput(attrs={'size': 40, 'placeholder': 'admin'}))
    password = forms.CharField(label='Password', max_length=100, required=False, widget=forms.PasswordInput(attrs={'size': 40, 'placeholder': 'password'}))
