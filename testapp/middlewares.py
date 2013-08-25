import datetime
from django.http import HttpResponse

from models import RequestLogs


class RequestSaverMiddleware(object):
    def process_request(self, request):
        RequestLogs(url=request.get_full_path(),
                    method=request.method,
                    time_stamp=datetime.datetime.now()).save()
