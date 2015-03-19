from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    def __unicode__(self):
	return unicode(self.name)

	
