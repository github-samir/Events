from django.contrib import admin
from . import models as m

# Register your models here.

admin.site.register(m.Member)
admin.site.register(m.Venue)
admin.site.register(m.Event)