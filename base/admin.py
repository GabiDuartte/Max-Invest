from django.contrib import admin
from .models import Investment

# Register your models here.

admin.site.register(Investment)
admin.site.register(Investor, admin.ModelAdmin)
