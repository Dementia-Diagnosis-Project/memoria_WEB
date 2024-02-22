from django.db import models

# Create your models here.
class Patients(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    name = models.CharField(max_length=10)
    birth = models.CharField(max_length=12)
    gender = models.CharField(max_length=2)

    smoking = models.BooleanField(default=False)
    drinking = models.BooleanField(default=False)
    depression = models.BooleanField(default=False)

    specific = models.CharField(max_length=20)


class Diagnosis(models.Model):
    id = models.CharField(primary_key=True, max_length=18)

    date = models.CharField(max_length=12)
    mmse = models.IntegerField(default=0)
    hippo = models.FloatField(default=0)

    mri = models.ImageField(upload_to='manager/data')