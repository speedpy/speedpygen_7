from django.urls import path
from .views import crud

urlpatterns = [
    # Timer URLs
    path('timer/', crud.TimerListView.as_view(), name='timer_list'),
    path('timer/<int:pk>/', crud.TimerDetailView.as_view(), name='timer_detail'),
    path('timer/create/', crud.TimerCreateView.as_view(), name='timer_create'),
    path('timer/<int:pk>/update/', crud.TimerUpdateView.as_view(), name='timer_update'),
    path('timer/<int:pk>/delete/', crud.TimerDeleteView.as_view(), name='timer_delete'),

    # TimerPreset URLs
    path('timerpreset/', crud.TimerPresetListView.as_view(), name='timerpreset_list'),
    path('timerpreset/<int:pk>/', crud.TimerPresetDetailView.as_view(), name='timerpreset_detail'),
    path('timerpreset/create/', crud.TimerPresetCreateView.as_view(), name='timerpreset_create'),
    path('timerpreset/<int:pk>/update/', crud.TimerPresetUpdateView.as_view(), name='timerpreset_update'),
    path('timerpreset/<int:pk>/delete/', crud.TimerPresetDeleteView.as_view(), name='timerpreset_delete'),

    # TimerEvent URLs
    path('timerevent/', crud.TimerEventListView.as_view(), name='timerevent_list'),
    path('timerevent/<int:pk>/', crud.TimerEventDetailView.as_view(), name='timerevent_detail'),
    path('timerevent/create/', crud.TimerEventCreateView.as_view(), name='timerevent_create'),
    path('timerevent/<int:pk>/update/', crud.TimerEventUpdateView.as_view(), name='timerevent_update'),
    path('timerevent/<int:pk>/delete/', crud.TimerEventDeleteView.as_view(), name='timerevent_delete'),

    # TimerAccess URLs
    path('timeraccess/', crud.TimerAccessListView.as_view(), name='timeraccess_list'),
    path('timeraccess/<int:pk>/', crud.TimerAccessDetailView.as_view(), name='timeraccess_detail'),
    path('timeraccess/create/', crud.TimerAccessCreateView.as_view(), name='timeraccess_create'),
    path('timeraccess/<int:pk>/update/', crud.TimerAccessUpdateView.as_view(), name='timeraccess_update'),
    path('timeraccess/<int:pk>/delete/', crud.TimerAccessDeleteView.as_view(), name='timeraccess_delete'),

]