import PIL
from keras.model import load_model
from PIL import Image, ImageOps
import numpy as np

def get_class(image_path, model_path, labels_path):
    np.set_printoptions(suppress=True)

    model = load_model(model_path, compile=False)

    class_names = open(labels_path, "r", encoding="utf-8").readlines()


    datos = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


    image = image.open(image_path).convert("RGB")


    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)


    array_imagen = np.asarray(image)


    array_imagen_normalized = (array_imagen.astype(np.float32) / 127.5) - 1


    datos[0] = array_imagen_normalized


    predicción = model.predict(datos)
    index = np.argmax(predicción)
    class_names = class_names[index]
    confidence_score = predicción[0][index]


    return (class_names[2:], confidence_score)