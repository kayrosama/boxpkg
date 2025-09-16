import logging
from django.http import HttpResponseForbidden

logger = logging.getLogger('honeypot')

class HoneypotMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in ['/admin123/', '/cgi-bin/']:
            logger.warning(f"HONEYPOT: acceso bloqueado a {request.path} desde {request.META.get('HTTP_USER_AGENT', '')}")
            return HttpResponseForbidden("Acceso denegado")
        return self.get_response(request)

