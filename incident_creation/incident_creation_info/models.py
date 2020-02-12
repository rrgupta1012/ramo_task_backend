from django.db import models


class IncidentCreationInfo(models.Model):
    first_name = models.CharField('First Name', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.first_name






