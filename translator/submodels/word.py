from django.db import models
from translation.models import WordFunction
from translation.models import Language

class Word(models.Model):
	word = models.CharField(max_length=200)
	date_added = models.DateTimeField('Date Added')
	language = models.ForeignKey(Language)
	word_function = models.ForeignKey(WordFunction)