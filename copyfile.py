import os
from shutil import copyfile
from os import listdir
from os.path import isfile, join
src_path = '/data/img/'
dstPath = '/data/tmp/'
onlyfiles = [f for f in listdir(src_path) if isfile(join(src_path, f))]
for i in xrange (10000):
    copyfile(join(src_path,onlyfiles[i]), dstPath)
