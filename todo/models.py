from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=200)

class Todo(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)