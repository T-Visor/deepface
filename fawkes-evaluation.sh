#!/bin/sh

# VGG-Face
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m VGG-Face -o fawkes-vggface-1.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m VGG-Face -o fawkes-vggface-2.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m VGG-Face -o fawkes-vggface-3.txt

# FaceNet
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m Facenet512 -o fawkes-facenet-1.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m Facenet512 -o fawkes-facenet-2.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m Facenet512 -o fawkes-facenet-3.txt

# ArcFace
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m ArcFace -o fawkes-arcface-1.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m ArcFace -o fawkes-arcface-2.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m ArcFace -o fawkes-arcface-3.txt

# Ensemble
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m Ensemble -o fawkes-ensemble-1.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m Ensemble -o fawkes-ensemble-2.txt
python3 run.py -s images/fawkes-imgs/ -d images/original-facescrub/ -k 5 -m Ensemble -o fawkes-ensemble-3.txt
