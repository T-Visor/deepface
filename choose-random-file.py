#!/usr/bin/env python3
import os
import random


# Reference: https://stackoverflow.com/questions/71873989/how-to-select-single-random-file-from-each-sub-directory-in-python
source_directory = './images/original-images/'
parent_folders = None
selected_images = []

# Select a random file from each subdirectory and store the subdirectories
for root, directories, files in os.walk(source_directory):
    if directories:
        parent_folders = directories
    if not files: continue
    selected_images.append(random.choice(files))

for image in selected_images:
    print(image)
