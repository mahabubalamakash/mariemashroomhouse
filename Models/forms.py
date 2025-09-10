from django.contrib.auth.forms import (User,UserChangeForm,UserCreationForm,)
from django import (forms,middleware,setup)



class register_forms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
