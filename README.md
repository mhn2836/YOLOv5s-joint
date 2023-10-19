## YOLOv5s-joint

  <p>YOLOv5s-joint是一个基于PyTorch的改进YOLOv5s和去雾算法的联合方法，能够实现默认YOLO分辨率的实时的去雾-检测功能。</p>

### Training：

在原版YOLOv5s基础上进行功能增加，加入j_training参数，可训练联合去雾检测模型。建议先行预训练去雾模型后，再进行联合训练。

运行命令 python train.py。 网络模型文件放在configs下。

训练模型可在./run文件夹下找到。
### Detection：

打开Joint参数即可实现联合去雾与检测。  

## Related work
  <p> https://github.com/mhn2836/dehaze</p>


