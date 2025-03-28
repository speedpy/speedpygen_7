from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from mainapp.models import *
from django import forms

class TimerListView(ListView):
    model = Timer
    template_name = 'mainapp/timer_list.html'
    context_object_name = 'timer_list'

class TimerDetailView(DetailView):
    model = Timer
    template_name = 'mainapp/timer_detail.html'
    context_object_name = 'timer'

class TimerCreateView(CreateView):
    model = Timer
    fields = ['name', 'duration', 'start_time', 'end_time', 'is_active', 'owner', 'access_code']

    template_name = 'mainapp/timer_form.html'
    success_url = reverse_lazy('timer_list')

class TimerUpdateView(UpdateView):
    model = Timer
    fields = ['name', 'duration', 'start_time', 'end_time', 'is_active', 'owner', 'access_code']

    template_name = 'mainapp/timer_form.html'
    success_url = reverse_lazy('timer_list')

class TimerDeleteView(DeleteView):
    model = Timer
    template_name = 'mainapp/timer_confirm_delete.html'
    success_url = reverse_lazy('timer_list')

class TimerPresetListView(ListView):
    model = TimerPreset
    template_name = 'mainapp/timerpreset_list.html'
    context_object_name = 'timerpreset_list'

class TimerPresetDetailView(DetailView):
    model = TimerPreset
    template_name = 'mainapp/timerpreset_detail.html'
    context_object_name = 'timerpreset'

class TimerPresetCreateView(CreateView):
    model = TimerPreset
    fields = ['name', 'duration', 'owner']

    template_name = 'mainapp/timerpreset_form.html'
    success_url = reverse_lazy('timerpreset_list')

class TimerPresetUpdateView(UpdateView):
    model = TimerPreset
    fields = ['name', 'duration', 'owner']

    template_name = 'mainapp/timerpreset_form.html'
    success_url = reverse_lazy('timerpreset_list')

class TimerPresetDeleteView(DeleteView):
    model = TimerPreset
    template_name = 'mainapp/timerpreset_confirm_delete.html'
    success_url = reverse_lazy('timerpreset_list')

class TimerEventListView(ListView):
    model = TimerEvent
    template_name = 'mainapp/timerevent_list.html'
    context_object_name = 'timerevent_list'

class TimerEventDetailView(DetailView):
    model = TimerEvent
    template_name = 'mainapp/timerevent_detail.html'
    context_object_name = 'timerevent'

class TimerEventCreateView(CreateView):
    model = TimerEvent
    fields = ['timer', 'event_type', 'timestamp']

    template_name = 'mainapp/timerevent_form.html'
    success_url = reverse_lazy('timerevent_list')

class TimerEventUpdateView(UpdateView):
    model = TimerEvent
    fields = ['timer', 'event_type', 'timestamp']

    template_name = 'mainapp/timerevent_form.html'
    success_url = reverse_lazy('timerevent_list')

class TimerEventDeleteView(DeleteView):
    model = TimerEvent
    template_name = 'mainapp/timerevent_confirm_delete.html'
    success_url = reverse_lazy('timerevent_list')

class TimerAccessListView(ListView):
    model = TimerAccess
    template_name = 'mainapp/timeraccess_list.html'
    context_object_name = 'timeraccess_list'

class TimerAccessDetailView(DetailView):
    model = TimerAccess
    template_name = 'mainapp/timeraccess_detail.html'
    context_object_name = 'timeraccess'

class TimerAccessCreateView(CreateView):
    model = TimerAccess
    fields = ['timer', 'user', 'access_type']

    template_name = 'mainapp/timeraccess_form.html'
    success_url = reverse_lazy('timeraccess_list')

class TimerAccessUpdateView(UpdateView):
    model = TimerAccess
    fields = ['timer', 'user', 'access_type']

    template_name = 'mainapp/timeraccess_form.html'
    success_url = reverse_lazy('timeraccess_list')

class TimerAccessDeleteView(DeleteView):
    model = TimerAccess
    template_name = 'mainapp/timeraccess_confirm_delete.html'
    success_url = reverse_lazy('timeraccess_list')
