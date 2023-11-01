from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone', 'gender')
