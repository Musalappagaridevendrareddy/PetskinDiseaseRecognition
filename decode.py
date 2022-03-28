import base64


def decodeImage(imgstring):
    imgdata = base64.b64decode(imgstring)
    with open('data.jpg', 'wb') as f:
        f.write(imgdata)
        f.close()
