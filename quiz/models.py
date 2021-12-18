from django.db import models

# Create your models here.

class Quiz(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	body = models.TextField()
	answer = models.IntegerField()
	
	class Meta:
		db_table = 'quiz'
