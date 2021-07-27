from django.contrib import admin
from .models import Document
from .models import Translation

admin.site.register(Document)
admin.site.register(Translation)
