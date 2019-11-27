from django.contrib import admin

# Register your models here.
# from django.contrib import admin

from .models import Option, Riddle
from .models import Message
admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Message)