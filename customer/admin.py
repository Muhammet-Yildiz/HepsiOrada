from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display= ["id","user","birthday","phone"]
    list_display_links = ["id","user"]


  