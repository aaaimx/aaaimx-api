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
NORWESTER = LOCATION("utils/fonts/Norwester.otf")
MONSERRAT = LOCATION("utils/fonts/Montserrat-Black.otf")


def SPARTAN_FONT(size): return ImageFont.truetype(SPARTAN, size)
def COPPER_FONT(size): return ImageFont.truetype(COOPER, size)


def generate_qr(url, size=5):
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
    Generate certificate from clean template
    '''
    # Create Certifcate image from template
    # get image sizes for calculations
    img = Image.open(LOCATION("utils/tmp/clean_cert.png"))
    widthImg, heightImg = img.size
    draw = ImageDraw.Draw(img)

    # Certificate type
    TYPE = "CERTIFICATE OF %s" % type
    typeWidth = SPARTAN_FONT(75).getsize(TYPE)[0]
    draw.text(((widthImg - typeWidth) / 2, 350),
              TYPE, '#003138', font=SPARTAN_FONT(75))

    # Participant name
    nameWidth = SPARTAN_FONT(92).getsize(name)[0]
    draw.text(((widthImg - nameWidth) / 2, 620),
              name, '#800000', font=SPARTAN_FONT(92))

    # Certificate UUID
    draw.text((100, 1270), 'Certificate ID: %s' % str(
        uuid), "#737373", font=ImageFont.truetype(ARIMO, 30))

    # Certificate description multiline
    lines = textwrap.wrap(desc, width=70)
    desc_font_size = 40
    desc_start_at = 770
    for line in lines:
        width, height = COPPER_FONT(desc_font_size).getsize(line)
        draw.text(((widthImg - width) / 2, desc_start_at), line,
                  "#003138", font=COPPER_FONT(desc_font_size))
        desc_start_at += height + 10

    # Certificate QR
    QR = generate_qr(url)
    img.paste(QR, (1690, 1050))

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
    print(widthImg, widthAvatar)
    img.paste(QR, (int((widthImg - widthQr) / 2), 440))
    img.paste(avatar, (300 + int((150 - widthAvatar) / 2), 170))
    output = LOCATION('utils/membership.png')
    img.save(output)
