#!/usr/bin/env python3

import sys
import subprocess
import os
from tqdm import tqdm
from pathlib import Path




source_directory = 'images/lowkey-imgs'
results = [os.path.join(dp, f) for dp, dn, fn in os.walk(source_directory) for f in fn]
value = 0

with tqdm(total=len(results)) as progress_bar:
    for item in results:
        returned = subprocess.call([sys.executable, 'run.py', '-s', item, '-d', 'images/original-images'])
        progress_bar.update(1)
