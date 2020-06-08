from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFile as PILImageFile
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from io import BytesIO, StringIO
import qrcode
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def LOCATION(file): return os.path.join(BASE_DIR, file)


# font files
SPARTAN = LOCATION("utils/fonts/LeagueSpartan-Bold.otf")
ARIMO = LOCATION("utils/fonts/Arimo-Regular.ttf")
COOPER = LOCATION("utils/fonts/CooperHewitt-Light.otf")
NORWESTER = LOCATION("utils/fonts/Norwester.otf")
MONSERRAT = LOCATION("utils/fonts/Montserrat-Black.otf")


def SPARTAN_FONT(size): return ImageFont.truetype(SPARTAN, size)


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


def generate_cert(name, type, uuid, url):
    TYPE = "CERTIFICATE OF {0}".format(type)
    img = Image.open(LOCATION("utils/tmp/clean_cert.png"))
    widthImg, heightImg = img.size
    typeWidth = SPARTAN_FONT(75).getsize(TYPE)[0]
    nameWidth = SPARTAN_FONT(92).getsize(name)[0]

    draw = ImageDraw.Draw(img)
    draw.text(((widthImg - typeWidth) / 2, 350),
              TYPE, '#003138', font=SPARTAN_FONT(75))
    draw.text(((widthImg - nameWidth) / 2, 620),
              name, '#800000', font=SPARTAN_FONT(92))
    draw.text((100, 1270), 'Certificate ID: {0}'.format(
        uuid), "#737373", font=ImageFont.truetype(ARIMO, 30))

    QR = generate_qr(url)
    img.paste(QR, (1690, 1050))
    output = LOCATION('utils/certificate.png')
    img.save(output)
    return ImageFile(open(output, 'rb+'))


def generate_membership(name, uuid, url, avatar=LOCATION("utils/foto.jpg")):
    img = Image.open(LOCATION("utils/tmp/clean_membership.png"))
    widthImg, heightImg = img.size

    draw = ImageDraw.Draw(img)
    draw.text((65, 350), name.upper(),
              "#fff", font=ImageFont.truetype(NORWESTER, 70))
    draw.text((300, 1850), 'ID: {0}'.format(uuid),
              "#fff", font=ImageFont.truetype(MONSERRAT, 35))

    QR = generate_qr(url, 13)
    size = 500, 500
    widthQr, heightQr = QR.size
    avatar = Image.open(avatar)
    avatar.thumbnail(size)
    img.paste(QR, (int((widthImg - widthQr) / 2), 1300))
    # img.paste(avatar, (920, 530))
    output = LOCATION('utils/membership-out.png')
    img.save(output)
    return ImageFile(open(output, 'rb+'))

