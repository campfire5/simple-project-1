from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=300)
	body = models.TextField(max_length=2000)
	date = models.DateTimeField()

	def __str__(self):
		return self.title