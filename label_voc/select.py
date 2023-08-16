import xml.etree.ElementTree as ET
import os
from os import getcwd
import shutil

test_path = r'/home/think/PycharmProjects/yoloair_fogcity/dehaze_test/images'
img_path = r'/home/think/PycharmProjects/yoloair_fogcity/cityscape_train/images'

final_path = r'/home/think/PycharmProjects/yoloair_fogcity/cityscape_test/images'

# aachen_000000_000019_leftImg8bit
# aachen_000006_000019_leftImg8bit_foggy_beta_0.005
def select1():
    test_list = []

    for test_file in os.listdir(test_path):
        test_list.append(test_file)
        # print(os.path.join(test_path, test_file))
        # print(test_file[:-3])

        #print(t)



    i = 0

    for img_file in os.listdir(img_path):
        # test_list.append(img_file)
        # i += 1



        if test_list.count(img_file) == 1:
            prev_path = os.path.join(img_path, img_file)

            new_path = os.path.join(final_path, img_file)
            shutil.move(prev_path, new_path)
            # i += 1

            print(new_path)


def select2():
    test_list = []

    for test_file in os.listdir(test_path):
        t = test_file[:-4]

        file = ''

        if t[-1] == '5':
            file = t[:-17]
            #print(t[:-17])
        else:
            file = t[:-16]
            #print(t[:-16])

        test_list.append(file + '.png')
        # print(os.path.join(test_path, test_file))
        # print(test_file[:-3])

        #print(t)
        #print('******************')

    i = 0

    for img_file in os.listdir(img_path):
        # test_list.append(img_file)
        # i += 1

        if test_list.count(img_file) == 1:
            prev_path = os.path.join(img_path, img_file)

            new_path = os.path.join(final_path, img_file)
            shutil.move(prev_path, new_path)
            i += 1

            print(new_path)
    print(i)

def rename():
    label_path = r'/home/think/PycharmProjects/yoloair_fogcity/cityscape_train/labels'

    for txt in os.listdir(label_path):
        # print(txt)

        t = txt[:-4]

        file = ''

        if t[-1] == '5':
            file = t[:-17]
            #print(t[:-17])
        else:
            file = t[:-16]
            #print(t[:-16])

        file += '.txt'

        prev_name = os.path.join(label_path, txt)

        new_name = os.path.join(label_path, file)

        #print(prev_name)
        print(new_name)

        #print('**************')

        os.rename(prev_name, new_name)

def check():
    image_path = r'/home/think/PycharmProjects/yoloair_fogcity/cityscape_train/images'
    label_path = r'/home/think/PycharmProjects/yoloair_fogcity/cityscape_train/labels'

    test_list = []

    for img in os.listdir(image_path):
        test_list.append(img)

    i = 0
    for label in os.listdir(label_path):
        if test_list.count(label[:-4] + '.png') == 0:
            print(label)



if __name__ == "__main__":
    # select2()
    # rename()
    check()