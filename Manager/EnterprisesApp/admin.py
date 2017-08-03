from django.contrib import admin

from .models import Enterprise

class AdminProfile(admin.ModelAdmin):
    class Meta:
        model = Enterprise


admin.site.register(Enterprise, AdminProfile)
