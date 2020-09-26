from django.http.response import HttpResponse, JsonResponse
from PIL import Image
from .main import AAAIMXStorage
from utils.images import LOCATION, generate_qr, generate_membership
import os

def image(request):
    # ... create/load image here ...
    image = Image.open(LOCATION("utils/certificate.png"))
    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    #response['Content-Length'] = str(len(response.content))
    image.save(response, 'PNG')
    return response


def membership(request):
    # ... create/load image here ...
    id = request.GET['id']
    nickname = request.GET['nickname']
    avatar = request.GET['avatar']
    generate_membership(nickname, id, id, avatar)
    return JsonResponse({})

def ftp_list(request):
    folder = request.GET.get('folder', '')
    ftp = AAAIMXStorage()
    ftp.login()
    folders = ftp.list(path=folder)
    return JsonResponse({'folders': folders})

def generate_QR(request):
    return 
