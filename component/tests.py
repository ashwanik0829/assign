import unittest
import os
from ml_component import process_csv_and_generate_model
from django.test import Client
from django.urls import reverse

class MLComponentTestCase(unittest.TestCase):
    def test_process_csv_and_generate_model(self):
        csv_file_path = 'path/to/csv/file.csv'
        target_column = 'target'
        
        model, evaluation_results = process_csv_and_generate_model(csv_file_path, target_column)
        
        self.assertIsNotNone(model)
        self.assertIsNotNone(evaluation_results)
        self.assertIsInstance(evaluation_results, float)

class DjangoAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_save_project_metadata(self):
        response = self.client.post(reverse('save_project_metadata'), {
            'tenant_id': '1',
            'local_csv_file_location': 'path/to/csv/file.csv',
            's3_model_location': 's3://your-bucket/model.pkl',
            'model_evaluation_results': '0.85'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'success': True})

    def test_get_tenant_and_project_metadata(self):
        response = self.client.get(reverse('get_tenant_and_project_metadata'))

        self.assertEqual(response.status_code, 200)
        self.assertTrue('tenant' in response.json())
        self.assertTrue('project_metadata' in response.json())

class MainScriptTestCase(unittest.TestCase):
    def test_main_script_workflow(self):
        os.environ['CSV_FILE_PATH'] = 'path/to/csv/file.csv'
        os.environ['TARGET_COLUMN'] = 'target'

        main_script_function()

        tenant_data = self.client.get(reverse('get_tenant_and_project_metadata')).json()['tenant']
        project_metadata_data = self.client.get(reverse('get_tenant_and_project_metadata')).json()['project_metadata']

        self.assertEqual(tenant_data['name'], 'John Doe')
        self.assertEqual(project_metadata_data['local_csv_file_location'], 'path/to/csv/file.csv')

if __name__ == '__main__':
    unittest.main()
