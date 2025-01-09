# models.py

from django.db import models
from django.contrib.auth.models import User

class VisitorLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    browser_info = models.CharField(max_length=255, blank=True)  # User-agent string
    referrer = models.URLField(blank=True)   # Referring URL (if applicable)
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for each visitor log entry

class BrowserInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Extract browser names from user-agent strings
    pattern = models.TextField()  # Regular expression to match the browser pattern in user-agents.

# views.py

from django.http import JsonResponse
from .models import VisitorLog, BrowserInfo

def log_visitor(request):
    ip_address = request.META.get('REMOTE_ADDR')
    ua_string = request.META.get('HTTP_USER_AGENT')
    
    # Extract browser information from the user-agent string
    browser_info, _ = BrowserInfo.objects.get_or_create(pattern=ua_string)

    visitor_log = VisitorLog(user=request.user if request.user else None,
                             ip_address=ip_address,
                             browser_info=browser_info.name if browser_info else 'Unknown',
                             referrer=request.META.get('HTTP_REFERER')
                            )
    visitor_log.save()
    
    return JsonResponse({'message': 'Visitor logged successfully!'}, status=201)

# urls.py

from django.urls import path
from .views import log_visitor

urlpatterns = [
    # ...
    path('log-visitor/', log_visitor, name='log_visitor'),
]
