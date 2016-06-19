from django.forms import ModelForm      
from .models import Images, Details, Events

class PhotoForm(ModelForm):
  class Meta:
      model = Images
      exclude = ('event',)

class RegisterForm(ModelForm):
    class Meta:
        model = Details
        exclude = ('user',)

class EventsForm(ModelForm):
    class Meta:
        model = Events
        exclude = ('creator','lat', 'lon', 'good')