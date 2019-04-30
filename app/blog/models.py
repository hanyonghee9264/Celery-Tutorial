from django.db import models


class Task(models.Model):
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return f'{self.start_at} - {self.end_at}'
