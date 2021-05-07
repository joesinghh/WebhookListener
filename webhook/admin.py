from django.contrib import admin
from .models import RequestDataJson, RequestDataText

# Register your models here.
admin.site.register(RequestDataJson)
admin.site.register(RequestDataText)

