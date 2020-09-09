from django.shortcuts import render,redirect
from django.contrib import messages
from . import models as m
from . import forms as f

# Create your views here.

def home(request):
  qs=m.Event.objects.order_by('-id')
  context={
    'events':qs,
  }
  return render(request,'home.html',context)

def eventDetail(request,event):
  qs=m.Event.objects.get(id=event)
  context={
    'event':qs
  }
  return render(request,'event_detail.html',context)

def createEvent(request):
  form = f.NewEventForm()
  if request.method == 'POST':
    form=f.NewEventForm(request.POST)
    if form.is_valid():
      event=form.save(commit=False)
      event.manager=m.Member.objects.get(id=1)
      event.save()
      messages.info(request,'Event is created.')
      return redirect('home')
  context={
    'form':form,
    
  }
  return render(request,'new_event.html',context)