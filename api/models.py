from django.db import models

# Create your models here.
class CrudItem(models.Model):
	id = models.AutoField(primary_key=True)
	# order = models.IntegerField(null=True, blank=True)
	text = models.CharField(max_length=256, null=True, blank=True)
	completed = models.BooleanField(blank=True, default=False)
	url = models.CharField(max_length=256, null=True, blank=True)
	