import textwrap
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFile as PILImageFile
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from io import BytesIO, StringIO
import qrcode
import os
import requests
from io import BytesIO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def LOCATION(file): return os.path.join(BASE_DIR, file)


# font files
SPARTAN = LOCATION("utils/fonts/LeagueSpartan-Bold.otf")
ARIMO = LOCATION("utils/fonts/Arimo-Regular.ttf")
COOPER = LOCATION("utils/fonts/CooperHewitt-Semibold.otf")
COOPER_LIGHT = LOCATION("utils/fonts/CooperHewitt-Light.otf")
NORWESTER = LOCATION("utils/fonts/Norwester.otf")
MONSERRAT = LOCATION("utils/fonts/Montserrat-Black.otf")


def SPARTAN_FONT(size):
    return ImageFont.truetype(SPARTAN, size)


def ARIMO_FONT(size):
    return ImageFont.truetype(ARIMO, size)


def COPPER_FONT(size):
    return ImageFont.truetype(COOPER, size)


def generate_qr(url, size=5):
    '''
    Returns a QR code image with URL
    '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def generate_cert(name, type, desc, uuid, url):
    '''
    Generate certificate from clean template (2000x1414px)
    '''

    # Create Certifcate image from template
    # get image sizes for calculations
    img = Image.open(LOCATION("utils/tmp/certificate_v1.png"))
    imgWidth, imgHeight = img.size
    cert_draw = ImageDraw.Draw(img)

    # Certificate type
    type_text = "CERTIFICATE OF %s" % type
    start_at = 350
    font_size = 75
    color = '#003138'
    width = SPARTAN_FONT(font_size).getsize(type_text)[0]
    cert_draw.text(((imgWidth - width) / 2, start_at),
                   type_text, color, font=SPARTAN_FONT(font_size))

    # Participant name
    start_at = 620
    color = '#800000'
    font_size = 92
    width = SPARTAN_FONT(font_size).getsize(name)[0]
    cert_draw.text(((imgWidth - width) / 2, start_at),
                   name, color, font=SPARTAN_FONT(font_size))

    # Certificate UUID
    uuid_text = 'Certificate ID: %s' % str(uuid)
    uuid_x = 100
    uuid_y = 1270
    font_size = 30
    color = "#737373"
    cert_draw.text((uuid_x, uuid_y), uuid_text,
                   color, font=ARIMO_FONT(font_size))

    # Certificate description multiline
    start_at = 770
    color = "#003138"
    font_size = 40
    line_space = 10
    lines = textwrap.wrap(desc, width=70)
    for line in lines:
        width, height = COPPER_FONT(font_size).getsize(line)
        cert_draw.text(((imgWidth - width) / 2, start_at), line,
                       color, font=COPPER_FONT(font_size))
        start_at += height + line_space

    # Certificate QR
    QR = generate_qr(url)
    QR_x = 1690
    QR_y = 1050
    img.paste(QR, (QR_x, QR_y))

    # save result and return as binary image
    output = LOCATION(f'utils/certificate.png')
    img.save(output)
    return ImageFile(open(output, 'rb+'))


def generate_membership(name, uuid, url, avatar):
    img = Image.open(LOCATION("utils/tmp/clean_membership.jpg"))
    widthImg, heightImg = img.size

    draw = ImageDraw.Draw(img)
    draw.text((30, 120), name.upper(),
              "#fff", font=ImageFont.truetype(NORWESTER, 35))
    draw.text((140, 625), 'ID: {0}'.format(uuid),
              "#fff", font=ImageFont.truetype(MONSERRAT, 15))

    QR = generate_qr(url, 6)
    size = 200, 200
    widthQr, heightQr = QR.size
    response = requests.get(avatar)
    avatar = Image.open(BytesIO(response.content))
    avatar.thumbnail(size, Image.ANTIALIAS)
    widthAvatar, heightAvatar = avatar.size
    img.paste(QR, (int((widthImg - widthQr) / 2), 440))
    img.paste(avatar, (300 + int((150 - widthAvatar) / 2), 170))
    output = LOCATION('utils/membership.png')
    img.save(output)
