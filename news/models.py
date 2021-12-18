from django.db import models

# Create your models here.
class News(models.Model):
	id = models.AutoField(primary_key=True)
	url = models.CharField(max_length=200)
	title = models.CharField(max_length=100)
	content = models.TextField(null=True)
	date = models.DateTimeField(null=True)
	photo = models.CharField(max_length=200, null=True)	

	class Meta:
		db_table = 'news'
