from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створення початкових даних для тестування моделі
        user = User.objects.create(username='testuser')
        Task.objects.create(title='Test Task', content='Test Content', user=user)

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Task')

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'To do')

    def test_user_foreign_key(self):
        task = Task.objects.get(id=1)
        user = User.objects.get(username='testuser')
        self.assertEquals(task.user, user)

    def test_str_method(self):
        task = Task.objects.get(id=1)
        self.assertEquals(str(task), 'Test Task')

    def test_get_absolute_url(self):
        task = Task.objects.get(id=1)
        expected_url = '/crate/1'  # Очікувана URL-адреса для об'єкта з id=1
        self.assertEquals(task.get_absolute_url(), expected_url)

    def test_verbose_name_plural(self):
        self.assertEquals(Task._meta.verbose_name_plural, 'Tasks')
