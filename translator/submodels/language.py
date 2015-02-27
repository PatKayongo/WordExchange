from django.db import models

class Language(models.Model):
	language_code = models.CharField(max_length=3)
	name = models.CharField(max_length=255)