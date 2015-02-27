from django.db import models

class Language(models.Model):
	language_code = models.CharField(max_length=3)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class WordFunction(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Word(models.Model):
	word = models.CharField(max_length=200)
	date_added = models.DateTimeField('Date Added')
	language = models.ForeignKey(Language)
	word_function = models.ForeignKey(WordFunction)

	def __str__(self):
		return self.word

class WordTranslation(models.Model):
	first_word = models.ForeignKey(Word, related_name="translation_first_word")
	second_word = models.ForeignKey(Word, related_name="translation_second_word")
	added_by_username = models.CharField(max_length=50)