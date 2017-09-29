# change image names to pure digits
import glob
import os

imgpath = './JPEGImages/'
annotpath = './Annotations'
imgsetspath = './ImageSets'
items = sorted(glob.glob(imgpath + '*.jpg'))

# scan each image, make changes
# name starts from 00000
namenum = 0
for item in items:
    # extract base name without extension
    basename = os.path.splitext(os.path.basename(item))[0]
    # change image name
    os.rename(os.path.join(imgpath, basename + '.jpg'), \
    os.path.join(imgpath, str(namenum).zfill(5) + '.jpg'))

    # change annotation name
    os.rename(os.path.join(annotpath, basename + '.xml'), \
    os.path.join(annotpath, str(namenum).zfill(5) + '.xml'))

    # name number increments
    namenum = namenum + 1

    
# change annotation file names accordingly

# pick 1/3 as train data, pick 1/3 as val data, pick 1/3 as test data

# create xxx_train.txt: 1 means xxx annotated, -1 means xxx not annotated

# create xxx_val.txt

# create xxx_traval.txt

# create xxx_test.txt
