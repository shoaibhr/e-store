from django.contrib import admin
from .models import Category, Product
# Register your models here.
models = [Category, Product]
for model in models:
    admin.site.register(model)