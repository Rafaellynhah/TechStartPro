from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

class ViewsTestCase(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.import_csv_url = reverse('import_csv')
        self.forms_url = reverse('forms')

    def test_list_response_200(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)  
        self.assertTemplateUsed(response, 'list.html') 

    def test_import_csv_response_200(self):
        response = self.client.get(self.import_csv_url)
        self.assertEquals(response.status_code, 200)  
        self.assertTemplateUsed(response, 'category_import.html') 

    def test_forms_response_200(self):
        response = self.client.get(self.forms_url)
        self.assertEquals(response.status_code, 200)  
        self.assertTemplateUsed(response, 'forms.html')              

