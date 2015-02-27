from django.db import models

class WordFunction(models.Model):
	name = models.CharField(max_length=50)