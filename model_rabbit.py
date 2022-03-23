from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

image=r"download (2).jpg"

def image_recog_rabbit(image):
    model = load_model('keras_model_rabbit.h5')


    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(image)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)


    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    arr = ["alopecia","mites","pododermatites","syphils","Ringworm","scabies"]
    prediction = arr[np.argmax(prediction)]
    return(prediction)


