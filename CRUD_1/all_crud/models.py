from django.db import models

# Create your models here.
class stu_record(models.Model):
    rollNo=models.IntegerField(default=0)
    fullName=models.CharField(max_length=50)
    phoneNo=models.BigIntegerField()
    city=models.CharField(max_length=50)
    course=models.CharField(max_length=20)
