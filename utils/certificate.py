from PIL import Image, ImageFont, ImageDraw
from django.core.files.images import ImageFile
import qrcode
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCATION = lambda file: os.path.join(BASE_DIR, file) 

# font files
SPARTAN = LOCATION("utils/fonts/LeagueSpartan-Bold.otf")
ARIMO = LOCATION("utils/fonts/Arimo-Regular.ttf")
COOPER = LOCATION("utils/fonts/CooperHewitt-Light.otf")
SPARTAN_FONT = lambda size: ImageFont.truetype(SPARTAN, size)

def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
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
    draw.text(((widthImg - typeWidth) / 2, 350), TYPE, '#003138' ,font=SPARTAN_FONT(75))
    draw.text(((widthImg - nameWidth) / 2, 620), name, '#800000', font=SPARTAN_FONT(92))
    draw.text((100, 1270), 'Certificate ID: {0}'.format(uuid), "#737373", font=ImageFont.truetype(ARIMO, 30))

    QR = generate_qr(url)
    img.paste(QR, (1690, 1050))
    output = LOCATION('utils/sample-out.png')
    img.save(output)
    return ImageFile(open(output, 'rb+'))