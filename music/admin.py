from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


admin.site.unregister(Group)

# Register your models here.
# class ImageThumbnailAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'image',  'date',)
# admin.site.register(ImageThumbnail,ImageThumbnailAdmin)
