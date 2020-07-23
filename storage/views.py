from django.http.response import HttpResponse, JsonResponse
from PIL import Image
from .main import AAAIMXStorage
from utils.images import LOCATION, generate_qr
import os

def image(request):
    # ... create/load image here ...
    image = Image.open(LOCATION("utils/certificate.png"))
    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    #response['Content-Length'] = str(len(response.content))
    image.save(response, 'PNG')
    return response

def ftp_list(request):
    folder = request.GET.get('folder')
    ftp = AAAIMXStorage()
    ftp.login()
    folders = ftp.list(path=folder)
    return JsonResponse({'folders': folders})

def generate_QR(request):
    return 
