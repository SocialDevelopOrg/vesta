from django.forms import ModelForm      
from .models import Images

class PhotoForm(ModelForm):
  class Meta:
      model = Images
      exclude = ()