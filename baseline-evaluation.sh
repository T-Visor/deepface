#!/bin/sh

# VGG-Face
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m VGG-Face -o baseline-vggface-1.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m VGG-Face -o baseline-vggface-2.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m VGG-Face -o baseline-vggface-3.txt

# FaceNet
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m Facenet512 -o baseline-facenet-1.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m Facenet512 -o baseline-facenet-2.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m Facenet512 -o baseline-facenet-3.txt

# ArcFace
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m ArcFace -o baseline-arcface-1.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m ArcFace -o baseline-arcface-2.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m ArcFace -o baseline-arcface-3.txt

# Ensemble
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m Ensemble -o baseline-ensemble-1.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m Ensemble -o baseline-ensemble-2.txt
python3 run.py -s images/original-facescrub/ -d images/original-facescrub/ -k 5 -m Ensemble -o baseline-ensemble-3.txt
