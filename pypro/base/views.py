from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Ola Django_New</body></html>', content_type='text/html')
