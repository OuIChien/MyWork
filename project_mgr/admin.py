from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from froala_editor.widgets import FroalaEditor
from django.conf.urls.static import static

from project_mgr.models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'project',)
    list_display_links = ('id', 'number',)


class DevTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class DevModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class TaskAdminForm(forms.ModelForm):

    description = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Task
        fields = ('description', 'version', 'dev_type', 'dev_model', 'priority', 'product_liable', 'development_liable',
                  'progress', 'review_time', 'dev_start_time', 'dev_complete_time', 'test_start_time', 'release_time')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', '_get_description',)

    form = TaskAdminForm

    def _get_description(self, obj):
        return mark_safe(obj.description)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(DevType, DevTypeAdmin)
admin.site.register(DevModel, DevModelAdmin)
admin.site.register(Task, TaskAdmin)
