from django.urls import path
from . import views as v

urlpatterns=[
  path('',v.home,name='home'),
  path('event/<int:event>/',v.eventDetail,name='event-detail'),
  path('new_event/',v.createEvent,name='create-event'),
]