from django.test import TestCase
from django.contrib.auth.models import User

from todo.models import Project
# from django.urls import reverse

class ProjectEditViewTest(TestCase):

  def setUp(self):
    # create User
    User.objects.create_superuser('testuser1', 'test@email.com', '12345')
    self.project = Project.objects.create(name='Awesome project')
  
  def test_edit_form(self):
    self.client.login(username='testuser1', password='12345')
    resp = self.client.get('/admin/todo/project/%i/change/' % self.project.pk)
    self.assertEqual(resp.status_code, 200)
    self.assertContains(resp, '<h2>Todos</h2>')