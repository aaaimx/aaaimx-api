from django.http.response import HttpResponse, JsonResponse
from PIL import Image
from .main import AAAIMXStorage
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def LOCATION(file): return os.path.join(BASE_DIR, file)

def image(request):
    # ... create/load image here ...
    image = Image.open(LOCATION("utils/certificate.png"))
    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    #response['Content-Length'] = str(len(response.content))
    image.save(response, 'PNG')
    return response

def ftp_list(request):
    ftp = AAAIMXStorage()
    ftp.login()
    folders = ftp.list(path='certificates/')
    return JsonResponse({'folders': folders})
