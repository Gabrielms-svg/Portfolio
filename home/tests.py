from django.test import TestCase
from django.urls import reverse


class PortfolioPageTests(TestCase):
    def test_home_page_renders(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_renders(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_project_detail_pages_render(self):
        for name in ['project_waste_detect', 'project_cams', 'project_sysmon']:
            with self.subTest(name=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
