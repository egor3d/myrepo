from django.contrib import admin
from .models import Video, Comments


class VideoInline(admin.StackedInline):
    model = Comments
    extra = 1


class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_filter = ["Video_date"]


admin.site.register(Video, VideoAdmin)
# Register your models here.
