
from django.shortcuts import render
from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class =  ProfileCreationForm
    template_name = 'profileapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})


    def form_valid(self, form):
        temp_profile = form.save(commit=False) # 임시 데이터 저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class =  ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self): # 수정후 detail 페이지로 가도록 함
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

