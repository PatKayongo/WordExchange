from django.db import models
from translation.models import Word

class WordTranslation(models.Model):
	first_word = models.ForeignKey(Word)
	second_word = models.ForeignKey(Word)
	added_by_username = models.CharField(max_length=50)