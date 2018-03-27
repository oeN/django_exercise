from django.test import TestCase

from todo.models import Project, Todo

class ProjectModelTest(TestCase):

  def test_str_on_project(self):
    """
    Casting a Project to string return the project name
    """
    project = Project(name="Awesome project")
    self.assertEqual(str(project), 'Awesome project')

class TodoModelTest(TestCase):
  
  def test_str_on_todo(self):
    """
    Casting a Task to string return the project name and the task title
    """
    project = Project(name="Awesome project")
    todo = Todo(title="My first todo", project=project)
    self.assertEqual(str(project), 'Awesome project - My first todo')
