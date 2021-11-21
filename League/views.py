from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('League/index.html')
	context = {'data': "data",}
	return HttpResponse(template.render(context, request))

def score(request):
	template = loader.get_template('League/match_score.html')
	context = {'data': "data",}
	return HttpResponse(template.render(context, request))