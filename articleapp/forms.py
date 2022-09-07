from django.forms import ModelForm
from articleapp.models import Article
from django import forms
from projectapp.models import Project

class ArticleCreationForm(ModelForm):    #
    
    # WYSIWYG 적용 
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable text-left', 'style':'height:auto;'}))
    
    # project를 선택하지 않아도 제출이 될 수 있게 함
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    
    class Meta:
        model = Article
        fields = ['title', 'image', 'project','content']