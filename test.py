#!/usr/bin/env python3

from deepface import DeepFace

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
models = ['VGG-Face', 'Facenet', 'Facenet512', 'OpenFace', 'DeepFace', 'DeepID', 'ArcFace', 'Dlib']


results_dataframe = DeepFace.find(img_path = 'images/lowkey-imgs/Jared_Padalecki/Jared_Padalecki_51635._attacked.png',
                    db_path = 'images/original-images',
                    enforce_detection = False,
                    detector_backend = backends[3])

print(str(results_dataframe.head(5)))
