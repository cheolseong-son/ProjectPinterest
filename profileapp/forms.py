from django.forms import ModelForm
from .models import Profile

# model을 formmodel로 변환하기 위해 사용

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message'] 