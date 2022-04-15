import base64
from PIL import Image
import requests

def decodeImage(imgstring):
    im = Image.open(requests.get(
        imgstring,
        stream=True).raw)
    im.save('data.jpg')
    # imgdata = base64.b64decode(imgstring)
    # with open('data.jpg', 'wb') as f:
    #     f.write(imgdata)
    #     f.close()
