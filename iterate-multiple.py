#!/usr/bin/env python3

import sys
import subprocess
import os
from pathlib import Path



source_directory = 'images/lowkey-imgs'
results = [os.path.join(dp, f) for dp, dn, fn in os.walk(source_directory) for f in fn]

for item in results:
    print(item)
    subprocess.call([sys.executable, 'run.py', '-s', item, '-d', 'images/original-images'])
