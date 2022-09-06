from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project

# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')
    
    # 'user'와 'project' 한 쌍이 갖는 구독정보는 오직 하나만 존재하도록
    class Meta:
        unique_together = ('user', 'project')