from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse('<h1> homepage <h2>')

def about_view(request):
    return HttpResponse('<h1> about <h2>')


def contact_view(request):
    return HttpResponse('<h1> contact <h2>')

