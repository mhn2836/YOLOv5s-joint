import os
import random

trainval_percent = 0.12
train_percent = 1.0
xmlfilepath = '../haze_test/Annotations'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
trainval = random.sample(list, tv)

txt_train='../haze_test/ImageSets/train.txt'
if os.path.exists(txt_train):
    os.remove(txt_train)
else:
    open(txt_train,'w')

txt_val='../haze_test/ImageSets/val.txt'
if os.path.exists(txt_val):
    os.remove(txt_val)
else:
    open(txt_val,'w')

ftrain = open(txt_train, 'w')
fval = open(txt_val, 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    ftrain.write(name)
    if i in trainval:
        fval.write(name)

ftrain.close()
fval.close()
