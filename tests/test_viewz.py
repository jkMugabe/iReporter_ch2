import unittest
import json
from api import views
from api.views import app


class TestRedFlags(unittest.TestCase):
    def setUp(self):
        """initialise test client"""
        self.api_tester = app.test_client()

        self.redflag = {
            "createdBy": 1,
            "incidentType": "redflag record",
            "location": "Bukoto",
            "status": "accepted",
            "images": "corruption.jpg",
            "Videos": "corruption.mp4",
            "comment": "He asked me 2M to give me a job"
        }

    def test_hello(self):
        response = self.api_tester.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual('Together We Can Make Uganda CORRUPTION FREE', data['message'])

    def test_create_redflag(self):
        response = self.api_tester.post('/api/v1/POST/redflags', content_type='application/json',
                                        json=self.redflag)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)

    def test_get_redflags(self):
        resp = self.api_tester.post('/api/v1/POST/redflags', content_type='application/json',
                                    json=self.redflag)
        response = self.api_tester.get('/api/v1/GET/redflags')
        data1 = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data1['status'], 200)
        self.assertIn("accepted", data1["data"][0]["status"])
        self.assertIn(data1['data'][0]['Videos'], 'corruption.mp4')

    def test_get_redflag(self):
        resp = self.api_tester.post('/api/v1/POST/redflags', content_type='application/json',
                                    json=self.redflag)
        response = self.api_tester.get('/api/v1/GET/redflags/2')
        data1 = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_redflag_empty(self):
        response = self.api_tester.get('/api/v1/GET/redflags/5')
        data1 = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data1['status'], 404)
        self.assertEqual(data1['error'], 'Redflag with that ID is not available')

    def test_update_location(self):
        location = {'location': 'Ntungamo'}
        response = self.api_tester.patch('/api/v1/PATCH/redflags/1/edit_location', json=location)
        data1 = json.loads(response.data)
        self.assertEqual(response.status_code, 210)
        self.assertEqual(data1['message'], 'Updated red-flag record\'s location')
        self.assertEqual(data1['status'], 210)

    def test_update_comment(self):
        comment = {'comment': 'Stop asing for bribes'}
        response = self.api_tester.patch('/api/v1/PATCH/redflags/1/edit_comment', json=comment)
        data1 = json.loads(response.data)
        self.assertEqual(response.status_code, 210)
        self.assertEqual(data1['status'], 210)

    def test_delete_redflag(self):
        resp = self.api_tester.post('/api/v1/POST/redflags', content_type='application/json',
                                    json=self.redflag)
        response = self.api_tester.delete('/api/v1/DELETE/redflags/2')
        data1 = json.loads(response.data)
        self.assertEqual(response.status_code, 206)
        self.assertEqual(data1['status'], 206)
