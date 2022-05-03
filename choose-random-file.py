#!/usr/bin/env python3
import os
import random

for d, ds, fs in os.walk('./images/original-images'):
    if not fs: continue
    print(f"rd.choice(fs): {random.choice(fs)}")
