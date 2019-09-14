from django.db import models
from django.utils import timezone


class RecordEvent(models.Model):

    active = models.BooleanField()
    audio_start_time = models.IntegerField()
    guid = models.AutoField(primary_key=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.guid) + ": " + str(self.active)
