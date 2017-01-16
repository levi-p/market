from django.contrib import admin
from .models import Article_details,Comments,article_Comment

# Register your models here.
admin.site.register(Article_details)
admin.site.register(Comments)
admin.site.register(article_Comment)
