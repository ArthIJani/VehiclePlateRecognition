from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'upload_date')

admin.site.register(Video, VideoAdmin)


