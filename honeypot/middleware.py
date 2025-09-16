import os
from django.conf import settings
from django.http import HttpResponseForbidden

class HoneypotMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = os.path.join(settings.BASE_DIR, 'logs', 'honeypot.log')
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
    
    def __call__(self, request):
        if request.path in ['/admin123/', '/cgi-bin/']:
            with open(self.log_file, 'a') as log:
                log.write(f"HONEYPOT: acceso bloqueado a {request.path} desde {request.META.get('HTTP_USER_AGENT', '')}\n")
            return HttpResponseForbidden("Acceso denegado")
        return self.get_response(request)

