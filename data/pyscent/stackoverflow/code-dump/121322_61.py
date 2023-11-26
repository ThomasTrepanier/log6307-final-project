#forms.py
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.form import UserCreationForm
from some_app.validators import validate_email

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken."),params = {'value':value})

class UserRegistrationForm(UserCreationForm):
        email = forms.EmailField(validators = [validate_email])
        
        class Meta:
            model = User
        fields = ['username', 'email', 'password1', 'password2']    
    
