#!/bin/sh

# VGG-Face
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m VGG-Face -o lowkey-vggface-1.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m VGG-Face -o lowkey-vggface-2.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m VGG-Face -o lowkey-vggface-3.txt

# FaceNet
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m Facenet512 -o lowkey-facenet-1.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m Facenet512 -o lowkey-facenet-2.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m Facenet512 -o lowkey-facenet-3.txt

# ArcFace
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m ArcFace -o lowkey-arcface-1.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m ArcFace -o lowkey-arcface-2.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m ArcFace -o lowkey-arcface-3.txt

# Ensemble
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m Ensemble -o lowkey-ensemble-1.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m Ensemble -o lowkey-ensemble-2.txt
python3 run.py -s images/lowkey-imgs/ -d images/original-facescrub/ -k 5 -m Ensemble -o lowkey-ensemble-3.txt
