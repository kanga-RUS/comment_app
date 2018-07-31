from django.contrib import admin
from .models import *

models = [Region, City, Comment]

admin.site.register(models)
