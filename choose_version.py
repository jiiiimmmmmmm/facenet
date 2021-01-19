from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import shutil
import argparse
import sys

def copy_files(version):
    if version in ['1.7.0','2.0']:
        file_names = os.listdir('tensorflow-'+version)
        for file_name in file_names:
            src = os.path.join('tensorflow-'+version,file_name)
            des = file_name
            try:
                shutil.copy(src, des)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())
    else:
        print('please select the right version. 1.7.0 or 2.0')

def main(args):
    copy_files(args.version)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--version', type=str, help='Select the version to run')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))