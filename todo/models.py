from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Todo(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return " - ".join([str(self.project), self.title])