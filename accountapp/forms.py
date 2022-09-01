# 정보 업데이트 시 유저id는 업데이트 못하도록 비활성화
from django.contrib.auth.forms import UserCreationForm

class accountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True