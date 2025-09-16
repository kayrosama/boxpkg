from django.test import TestCase, Client
from django.conf import settings
import os

class HoneypotViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.log_file = os.path.join(settings.LOG_DIR, 'HoneyPot.log')
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        
        if os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.truncate(0)
                    
    def test_access_to_cgi_bin(self):
        response = self.client.get('/cgi-bin/', HTTP_USER_AGENT='test-agent')
        self.assertEqual(response.status_code, 403)
        self.assertIn(b"Acceso denegado", response.content)
        
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, 'r') as log:
            log_content = log.read()
            self.assertIn("HONEYPOT", log_content)
            self.assertIn("/cgi-bin/", log_content)
            self.assertIn("test-agent", log_content)
    
    def test_access_to_admin123(self):
        response = self.client.get('/admin123/', HTTP_USER_AGENT='malicious-bot')
        self.assertEqual(response.status_code, 403)
        self.assertIn(b"Acceso denegado", response.content)
        
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, 'r') as log:
            log_content = log.read()
            self.assertIn("HONEYPOT", log_content)
            self.assertIn("/admin123/", log_content)
            self.assertIn("malicious-bot", log_content)
        

