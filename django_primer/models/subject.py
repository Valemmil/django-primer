from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=20, null=False, primary_key=True)

    def __str__(self):
        return str(self.name)
