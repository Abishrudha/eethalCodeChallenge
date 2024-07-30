from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class VolunteerLog(models.Model):
    name = models.CharField(max_length=100)
    volunteerlog = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name