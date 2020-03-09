from PIL import Image

import os
import sys
from os.path import dirname, abspath, realpath

dir = dirname(realpath(__file__))

in_dir = dir + r"\dropfolder"

outfolder = dir + r"\outfolder"

filenames = []

for filename in os.listdir(in_dir):
    filenames.append(filename)

if len(filenames) > 1:
    print("There is more than one file in the inputs dropfolder--there are {}\
        files".format(len(filenames)))

for fn in filenames:
    if not(fn.endswith('.ico')):
        ico_fn = r"{}\{}ico".format(outfolder, fn.rstrip('png'))
        fn = r"{}\{}".format(in_dir, fn)
        img = Image.open(fn)
        img.save(ico_fn)
        print("Saved {}".format(ico_fn))

    
