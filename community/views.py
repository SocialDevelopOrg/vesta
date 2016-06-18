# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django import forms

from .models import Images
from .forms import PhotoForm


def index(request):
    return render_to_response('community/index.html')

def home(request):
    return render_to_response('community/home.html')


def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'community/upload.html', context)