from django.forms import ModelForm
from .models import User

class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'about', 'avatar']