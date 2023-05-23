from django.db import models

# Create your models here.
class Jobs(models.Model):
    title=models.TextField(max_length=1000)
    title = models.TextField(max_length=5000)
    link=models.URLField(max_length=1000)
    image=models.ImageField(max_length=2000)
    
class JobDetail(models.Model):
    job= models.ForeignKey(Jobs, related_name='job_details', on_delete=models.CASCADE)
    details=models.TextField(max_length=20000)
    bold=models.BooleanField(default=False)