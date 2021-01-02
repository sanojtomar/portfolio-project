from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
	title = models.CharField(default='',max_length=200)
	body = models.TextField(default='')
	pub_date = models.DateTimeField(default=datetime.now(), blank=True)
	image = models.ImageField(default='',upload_to='images/')


