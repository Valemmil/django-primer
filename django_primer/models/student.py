from django.db import models


class Student(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)

    class Meta:
        unique_together = (('id', 'name', 'surname'),)

    @property
    def fio(self):
        return f'{self.name} {self.surname}'
