import base64
from io import BytesIO

import cv2
# import dlib
import imutils
import numpy as np
from PIL import Image
from imutils import face_utils

import os

# import cStringIO
import logging,sys
# FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SHAPE_PREDICTOR_FILE = os.path.join(FILE_DIR, 'files/shape_predictor_68_face_landmarks.dat')
# predictor = dlib.shape_predictor(SHAPE_PREDICTOR_FILE)

# detector = dlib.get_frontal_face_detector()
center_coordinates = (120, 50)
radius = 100
color = (255, 255, 255)
thickness = 50


def base64_decode(data):
    format, imgstr = data.split(';base64,')
    return base64.b64decode(imgstr)


def base64_encode(data):
    if data:
        return 'data:image/png;base64,'+ data.decode('utf-8')


def get_face_detect_data(data):
    nparr = np.fromstring(base64_decode(data), np.uint8)
    # print(nparr, file=sys.stderr)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image_data = detectImage(img)
    # print(base64_encode(image_data),file=sys.stderr)
    return base64_encode(image_data)
    



def detectImage(image):
    image = imutils.resize(image, width=500)
    image = cv2.circle(image, center_coordinates, radius, color, thickness) 
    # rects = detector(image, 1)
    # for (i, rect) in enumerate(rects):
    #     (x, y, w, h) = face_utils.rect_to_bb(rect)
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     cv2.putText(image, "Face".format(i + 1), (x - 10, y - 10),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    if True:
        output = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        buffer = BytesIO()
        img = Image.fromarray(output)
        img.save(buffer, format="png")
        # print(buffer.getvalue(),file=sys.stderr)
        encoded_string = base64.b64encode(buffer.getvalue())
        # print(encoded_string,file=sys.stderr)
        return encoded_string
