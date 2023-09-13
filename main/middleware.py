import time
from django.http import HttpResponseForbidden
import re
from django.http import HttpResponse

from django.http import HttpResponseForbidden


class DDoSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests = {}

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        current_time = int(time.time())

        if ip in self.requests:
            requests_count = len([t for t in self.requests[ip] if t > current_time - 60])
            if requests_count > 100:  
                return HttpResponse('Too Many Requests', status=429)

            self.requests[ip].append(current_time)
        else:
            self.requests[ip] = [current_time]

        response = self.get_response(request)
        return response


# class MalwareProtectionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if self.has_malware(request):
#             return HttpResponseForbidden('Malware detected')

#         response = self.get_response(request)
#         return response
#     def has_malware(request):
#         dangerous_extensions = ['.php', '.exe', '.dll', '.py', '.sh']
#         dangerous_patterns = ['eval(', 'exec(', 'os.system(', 'shell_exec(']

#         for param in request.GET.values():
#             for extension in dangerous_extensions:
#                 if extension in param:
#                     return True

#         for pattern in dangerous_patterns:
#             if re.search(pattern, param):
#                 return True

#         for param in request.POST.values():
#             for extension in dangerous_extensions:
#                 if extension in param:
#                     return True

#         for pattern in dangerous_patterns:
#             if re.search(pattern, param):
#                 return True

#         return False



# class SQLInjectionMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if self.has_sql_injection(request):
#             return HttpResponseForbidden('SQL injection attempt detected')

#         response = self.get_response(request)
#         return response




