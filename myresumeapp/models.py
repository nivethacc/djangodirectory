from django.db import models

# Create your models here.
class RegistrationModels(models.Model):
	recruiter_name = models.CharField(max_length=120,null=True)
	company = models.CharField(max_length=120)
	email   = models.EmailField(null=True,blank=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.recruiter_name