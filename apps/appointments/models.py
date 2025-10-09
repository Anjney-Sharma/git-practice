from django.db import models


class Appointment(models.Model):
    provider_name = models.CharField(max_length=100)
    appointment_datetime = models.DateTimeField()
    client_email = models.EmailField()

    def __str__(self):
        return f"Appointment with {self.provider_name} at {self.appointment_datetime.strftime('%Y-%m-%d %H:%M')}"
