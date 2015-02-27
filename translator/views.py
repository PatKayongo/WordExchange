from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from translator.models import Language, WordFunction
from translator.serializers import LanguageSerializer, WordFunctionSerializer

class JSONResponse(HttpResponse):
	"""An HttpResponse that renders its content into JSON."""

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

def language_list(request):
	if (request.method == 'GET'):
		languages = Language.objects.all()
		serializer = LanguageSerializer(languages, many=True)
		return JSONResponse(serializer.data)

def word_functions(request):
	if (request.method == 'GET'):
		wordFunctions = WordFunction.objects.all()
		serializer = WordFunctionSerializer(wordFunctions, many=True)
		return JSONResponse(serializer.data)

# Create your views here.
