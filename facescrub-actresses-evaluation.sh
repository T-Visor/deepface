#!/bin/sh

# BASELINE
#====================================================================================================================
# VGG-Face
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o baseline-vggface-1.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o baseline-vggface-2.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o baseline-vggface-3.txt

# FaceNet
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o baseline-facenet-1.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o baseline-facenet-2.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o baseline-facenet-3.txt

# ArcFace
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o baseline-arcface-1.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o baseline-arcface-2.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o baseline-arcface-3.txt

# Ensemble
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o baseline-ensemble-1.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o baseline-ensemble-2.txt
python3 run.py -s images/facescrub-actresses/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o baseline-ensemble-3.txt

# FAWKES
#====================================================================================================================
# VGG-Face
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o fawkes-vggface-1.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o fawkes-vggface-2.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o fawkes-vggface-3.txt

# FaceNet
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o fawkes-facenet-1.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o fawkes-facenet-2.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o fawkes-facenet-3.txt

# ArcFace
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o fawkes-arcface-1.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o fawkes-arcface-2.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o fawkes-arcface-3.txt

# Ensemble
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o fawkes-ensemble-1.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o fawkes-ensemble-2.txt
python3 run.py -s images/facescrub-actresses-fawkes/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o fawkes-ensemble-3.txt

# LOWKEY
#====================================================================================================================
# VGG-Face
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o lowkey-vggface-1.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o lowkey-vggface-2.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m VGG-Face -o lowkey-vggface-3.txt

# FaceNet
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o lowkey-facenet-1.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o lowkey-facenet-2.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m Facenet512 -o lowkey-facenet-3.txt

# ArcFace
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o lowkey-arcface-1.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o lowkey-arcface-2.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m ArcFace -o lowkey-arcface-3.txt

# Ensemble
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o lowkey-ensemble-1.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o lowkey-ensemble-2.txt
python3 run.py -s images/facescrub-actresses-lowkey/ -d images/facescrub-actresses/ -k 5 -m Ensemble -o lowkey-ensemble-3.txt
