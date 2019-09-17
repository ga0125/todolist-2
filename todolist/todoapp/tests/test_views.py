from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.task_url = reverse('api')
        self.add_task_url = reverse('add-task')
        self.done_task_url = reverse('done-task')
        self.filed_task_url = reverse('filed-task')
        self.del_task_url = reverse('del-task')

    def test_task_list_GET(self):
        response = self.client.get(self.task_url)

        self.assertEquals(response.status_code, 200)

    def test_add_task_POST(self):
        response = self.client.post(self.add_task_url, {
            'title': 'Unit test',
            'desc': 'Testing the APIs calls by unit test',
            'deadline': '2019-09-14',
        })

        self.assertEquals(response.status_code, 302)

    def test_done_task_POST(self):
        date = datetime.now()

        response = self.client.post(self.done_task_url, {
            'id': 1,
            'complete': True,
            'completed_at': date
        })

        self.assertEquals(response.status_code, 201)

    def test_filed_task_POST(self):
        response = self.client.post(self.filed_task_url, {
            'id': 1,
            'filed': True
        })

        self.assertEquals(response.status_code, 201)

    def test_del_task_DEL(self):
        response = self.client.delete(self.del_task_url, {
            'id': 1
        })

        self.assertEquals(response.status_code, 200)
