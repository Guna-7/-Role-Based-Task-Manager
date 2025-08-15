from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks',null=True,blank=True)
    
    completion_note = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    ROLE_CHOICES = (('manager','Manager'),('emplyoyee','Employee'))
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES)
    
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"