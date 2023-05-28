from django.db import models

from .student import Student
from .subject import Subject


class Score(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.FloatField(blank=False, null=False)

    class Meta:
        unique_together = (('student', 'subject'),)
