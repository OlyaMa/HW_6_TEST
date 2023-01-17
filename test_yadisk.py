import unittest
from unittest import TestCase
import requests
from main import create_folder


class TestYaDisk(TestCase):

    def test_create_folder_a(self):
        response = create_folder('Folder')
        self.assertEqual(response.status_code, 201)

    @unittest.expectedFailure
    def test_create_folder_b(self):
        create_folder('Folder')
        resp = create_folder('Folder')
        self.assertEqual(resp.status_code, 201)

    @unittest.expectedFailure
    def test_create_folder_c(self):
        create_folder('Folder')
        token = "" # Необходимо указать токен
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        resp = requests.get(f'{URL}?path=Folder', headers=headers)
        self.assertEqual(resp.status_code, 404)
