from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, default =1, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	Gender_Choices = (
		('FEMALE', 'female'), 
		('MALE' ,'male')
		)
	name = models.CharField(max_length=120)
	gender = models.CharField(max_length=120, choices = Gender_Choices, default = 1 )
	date_of_birth = models.DateField()
	exam_grade = models.CharField(max_length=120)
	classroom = models.ForeignKey(Classroom, default =1, on_delete = models.CASCADE)

