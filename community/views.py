# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django import forms

from .models import Images
from .forms import PhotoForm, EventsForm, RegisterForm
from django.contrib.auth.decorators import login_required



def index(request):
    return render_to_response('community/index.html')

@login_required
def home(request):
    if not hasattr(request.user, 'details'):
        return index(request)
    name = request.user.first_name+" "+request.user.last_name
    pincode = request.user.details.pincode
    return render(request, 'community/home.html', {'name':name, 'pincode':pincode})

@login_required
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            reg = form.save(commit=False)
            reg.user = request.user
            reg.save()
            return home(request)
        else:
            print form
    else:
        if hasattr(request.user, 'details'):
            return home(request)
        form = RegisterForm()
    return render(request, 'community/register.html', {'form':form, 'name':request.user.first_name+" "+request.user.last_name, \
     'email':request.user.email})

def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()
  return render(request, 'community/upload.html', context)

@login_required
def add(request):
    if request.method=='POST':
        eventform = EventsForm(request.POST, prefix="eventform")
        # photoform = PhotoForm(request.POST, request.FILES, prefix="photoform")
        # print photoform
        if eventform.is_valid():# and photoform.is_valid():
            event = eventform.save(commit=False)
            event.creator = request.user
            # define lat, lon, good
            event.save()

            # photo = photoform.save(commit=False)
            # photo.event = event
            # photo.save()
            return home(request)
        else:
            print eventform.errors
            print
            # print photoform.errors
    else:
        eventform = EventsForm(prefix="eventform")
        # photoform = PhotoForm(prefix="photoform")
    return render(request, 'community/add.html', {'eventform':eventform, \
        'name':request.user.first_name+" "+request.user.last_name, \
        'pincode':request.user.details.pincode})#, 'photoform':photoform})