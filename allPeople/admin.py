from django.contrib import admin
from .models import Message
from .models import Followers

# Register your models here.
admin.site.register(Message)
admin.site.register(Followers)

