# import mini_unet.network

# import mini_unet
#from mini_unet.unet_model import
#from mini_unet.unet_model_mini import *
from mini_unet.network import Pre_encoder
from models.yolo import Model

import torch
import torch.nn as nn


if __name__ == '__main__':

    yolo_net = torch.load('j_model/yolo.pt', map_location='cpu')

    yolo_model = yolo_net['model'].state_dict()

    dehaze_net = Pre_encoder()
    dehaze_net.load_state_dict(torch.load('j_model/foggy_city.pth'))
    dehaze_model = dehaze_net.state_dict()

    temp = dehaze_model

    ckpt = torch.load('j_model/joint.pt', map_location='cpu')

    res = ckpt['model'].state_dict()

    for key in dehaze_model:
        t = 'model.0.' + key
        res[t] = dehaze_model[key]


    dehaze_len = len(dehaze_model)
    
    yolo_len = len(yolo_model)

    temp = []

    for key in yolo_model:
        temp.append(yolo_model[key])

    i = 0



    for key in ckpt['model'].state_dict():
        if i >= dehaze_len:

            res[key] = temp[i - dehaze_len]

        i += 1

    new_pt = ckpt

    new_pt['model'].load_state_dict(res, strict= False)

    torch.save(new_pt, 'joint.pt')


    '''
    model1 = Pre_encoder()
    model2 = Model('./configs/test/yolov5s.yaml', ch=3, nc=5, anchors=3).cuda()

    net = joint_net(model1, model2)

    print(net.state_dict())
    
    dehaze_net = Pre_encoder()                            
    dehaze_net.load_state_dict(torch.load('j_model/dehaze.pth'))
    dehaze_model = dehaze_net.state_dict()
    print(dehaze_net.state_dict())

# print(dehaze_model)

# print(model['model'].state_dict())

    temp = dehaze_model
    # temp.update(yolo_model)
    ckpt = torch.load('joint.pt', map_location='cpu')
    # print(ckpt['model'])
    res = ckpt['model'].state_dict()

    # print(temp)    done
    for key in dehaze_model:
        t = 'model.0.' + key
        res[t] = dehaze_model[key]



    dehaze_len = len(dehaze_model)


    print(len(temp))

    i = 0

    # print(torch.typename(temp[0]))

    new_pt = ckpt

    new_pt['model'].load_state_dict(res, strict= False)  

    test = torch.load('test.pt')
    #print(test['model'].state_dict())
    #torch.save(new_pt, 'new.pt')
    '''