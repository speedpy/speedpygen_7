from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
class Timer(models.Model):
    name = models.CharField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default='False')
    owner = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="owner_timers")
    access_code = models.CharField(blank=False, null=False, unique=True)
    def __str__(self):
        return str(self.name)

class TimerPreset(models.Model):
    name = models.CharField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    owner = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="owner_timerpresets")
    def __str__(self):
        return str(self.name)

class TimerEvent(models.Model):
    timer = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Timer", related_name="timer_timerevents")
    event_type = models.CharField(blank=False, null=False)
    timestamp = models.DateTimeField(blank=False, null=False)
    def __str__(self):
        return str(self.id)

class TimerAccess(models.Model):
    timer = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Timer", related_name="timer_timeraccesss")
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_timeraccesss")
    access_type = models.CharField(blank=False, null=False)
    def __str__(self):
        return str(self.id)
