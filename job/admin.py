from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = admin

    search_fields = ('developer__username', 'created_by__username',)
    list_display = (
    'name', 'description', 'status', 'developer', 'created_by', 'creation_time', 'modification_time', 'image_banner')
    list_filter = ('name', 'status')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False





