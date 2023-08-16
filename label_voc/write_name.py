import xml.etree.ElementTree as ET
import os
from os import getcwd
import shutil

def write_txt(path, txt_path):
    txt = txt_path + 'object.txt'

    if os.path.exists(txt):
        os.remove(txt)
    else:
        open(txt, 'w')

    ftxt = open(txt, 'w')
    for file in os.listdir(path + '/images'):
        # t = txt_path + 'images/' + file
        t = path + '/images/' + file

        print(t[3:])
        ftxt.write(t[3:] + '\n')

    ftxt.close()

if __name__ == "__main__":
    path = r'../cityscape_test'

    txt_path = r'../cityscape_train/'

    write_txt(path, txt_path)