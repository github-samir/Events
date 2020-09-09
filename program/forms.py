from django import forms
from .models import Event

class NewEventForm(forms.ModelForm):
  class Meta:
    model = Event
    exclude = ('attendes','manager')