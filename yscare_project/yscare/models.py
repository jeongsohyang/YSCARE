from django.db import models
from users.models import User

class GlucoseData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose_level = models.FloatField()
    measured_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.name} - {self.glucose_level}"


class SleepData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sleep_duration_minutes = models.IntegerField()
    recorded_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.name} - {self.sleep_duration_minutes} min"


class StepData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step_count = models.IntegerField()
    recorded_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.name} - {self.step_count} steps"


class HeartrateData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bpm = models.IntegerField()
    recorded_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.name} - {self.bpm} BPM"


class CoachingLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_summary = models.TextField()
    response_summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Coaching for {self.user.name} at {self.created_at}"
