# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('community/index.html')

def home(request):
    return render_to_response('community/home.html')