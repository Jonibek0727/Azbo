from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CostomUser, Arizalar
from django import forms

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    # is_admin = forms.BooleanField(required=False)
    is_operator = forms.BooleanField(required=False)
    is_shop = forms.BooleanField(required=False)
    is_shop_child = forms.BooleanField(required=False)
    class Meta:
        model = CostomUser
        fields = ['first_name', 'last_name', 'username', 'email','is_operator' ,'is_shop','is_shop_child','password1', 'password2']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Arizalar
        fields = ['first_name','last_name','tel','type_muddat','pasport_seria','data_user','pasport_photo']

