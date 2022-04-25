#!/usr/bin/env python3

import sys
import subprocess
import os
from tqdm import tqdm
from pathlib import Path




source_directory = 'images/lowkey-imgs/Adam_Brody'
results = [os.path.join(dp, f) for dp, dn, fn in os.walk(source_directory) for f in fn]
source_images_count = len(results)
correct_predictions = 0

# Create a blank file
open('sample.txt', mode='w').close()

with tqdm(total=source_images_count) as progress_bar:
    for item in results:
        returned = subprocess.call([sys.executable, 'run.py', '-s', item, '-d', 'images/original-images'])
        progress_bar.update(1)

out_file = open('sample.txt', mode='a')
percentage = round(100 * float(correct_predictions) / float(source_images_count))
percentage = str(percentage) + '%'
out_file.write('\nAccuracy: ' + str(correct_predictions) + '/' + str(source_images_count) + ' (' + percentage + ')')
