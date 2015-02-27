from django.forms import widgets
from rest_framework import serializers
from translator.models import Language, WordFunction

class LanguageSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	language_code = serializers.CharField(required=True, allow_blank=False, max_length=3)
	name = serializers.CharField(required=True, allow_blank=False, max_length=255)

	def create(self, validated_data):
		return Language.objects.create(**validated_data)

	def create(self, instance, validated_data):
		instance.language_code = validated_data.get('language_code', instance.language_code)
		instance.name = validated_data.get('name', instance.name)

class WordFunctionSerializer(serializers.ModelSerializer):
	class Meta:
		model = WordFunction
		fields = ('id', 'name')