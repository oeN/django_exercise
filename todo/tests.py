from django.test import TestCase

from .models import Project

class ProjectModelTest(TestCase):

  def test_str_a_project_return_the_project_name(self):
    """
    Casting a Project to string return the project name
    """
    project = Project(name="Awesome project")
    self.assertEqual(str(project), 'Awesome project')
