from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todoapp.views import index, add_task, done_task, filed_task, del_task,  TasksApi

class UrlTest(SimpleTestCase):

    def test_api_url_resolves(self):
        url = reverse('api')
        self.assertEquals(resolve(url).func.view_class, TasksApi)

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_add_url_resolves(self):
        url = reverse('add-task')
        self.assertEquals(resolve(url).func, add_task)

    def test_done_url_resolves(self):
        url = reverse('done-task')
        self.assertEquals(resolve(url).func, done_task)

    def test_filed_url_resolves(self):
        url = reverse('filed-task')
        self.assertEquals(resolve(url).func, filed_task)

    def test_del_url_resolves(self):
        url = reverse('del-task')
        self.assertEquals(resolve(url).func, del_task)