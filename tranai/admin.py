from django.contrib import admin
from .models import Document
from .models import Translation
from .models import Task
# from .models import User
from .models import Sentence
from .models import Lookup

admin.site.register(Document)
admin.site.register(Translation)
admin.site.register(Task)
# admin.site.register(User)
admin.site.register(Sentence)
admin.site.register(Lookup)