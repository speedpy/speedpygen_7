from django.contrib import admin
from mainapp.models import *

@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'is_active', 'access_code']
    search_fields = ['name', 'access_code']

@admin.register(TimerPreset)
class TimerPresetAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
    search_fields = ['name']

@admin.register(TimerEvent)
class TimerEventAdmin(admin.ModelAdmin):
    list_display = ['event_type']
    search_fields = ['event_type']

@admin.register(TimerAccess)
class TimerAccessAdmin(admin.ModelAdmin):
    list_display = ['access_type']
    search_fields = ['access_type']
