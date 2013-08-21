from django.http import HttpResponse
from models import Hook_http


class HttpHookMiddleware(object):
    def process_request(self, request):
        Hook_http(http_request=request.build_absolute_uri()).save()