#codin:utf8
from config import opt
import os
import models
from skimage import io
from torch.autograd import Variable
from torchnet import meter
# from utils import Visualizer
from tqdm import tqdm
from torchvision import transforms
import torchvision
import torch
from torchsummary import summary
import json
import numpy as np
import cv2
class DataHandle():

    def __init__(self,scale=2.7,image_size=224,use_gpu=False,transform=None,data_source = None):
        self.transform = transform
        self.scale = scale
        self.image_size = image_size
        
    def det_img(self,imgdir):
        input = io.imread(imgdir)
        return preds

    def get_data(self,image_path):
        img = cv2.imread(image_path)
        return np.transpose(np.array(img, dtype = np.float32), (2, 0, 1)), image_path

    def __len__(self):
        return len(self.img_label)

def inference(image_path):
    import glob
    # images = glob.glob(kwargs['images'])
    # assert len(images)>0
    data_handle = DataHandle(
                        scale = opt.cropscale,
                        use_gpu = opt.use_gpu,
			transform = None,
			data_source='none')
    pths = glob.glob('Testing_Models/ultimate_dataset/MyMobilenetF/*.pth')
    pths.sort(key=os.path.getmtime,reverse=True)
    print(pths)
    # opt.parse(kwargs)
    # 模型
    opt.load_model_path=pths[0]
    model = getattr(models, opt.model)().eval()
    assert os.path.exists(opt.load_model_path)
    if opt.load_model_path:
       model.load(opt.load_model_path)
    if opt.use_gpu: model.cuda()
    model.train(False)
    data,_ = data_handle.get_data(image_path)
    data = data[np.newaxis,:]
    data = torch.FloatTensor(data)
    with torch.no_grad():
        if opt.use_gpu:
            data =  data.cuda()
        outputs = model(data)
        outputs = torch.softmax(outputs,dim=-1)
        preds = outputs.to('cpu').numpy()
        attack_prob = preds[:,opt.ATTACK]
        if attack_prob >0.4:
            return False, attack_prob
        else:
            return True, attack_prob


def help():
    '''
        python file.py help
    '''

    print('''
    usage : python {0} <function> [--args=value,]
    <function> := train | test | help
    example:
           python {0} train --env='env0701' --lr=0.01
           python {0} test --dataset='path/to/dataset/root/'
           python {0} inference --images='image dirs'
           python {0} help
    avaiable args:'''.format(__file__))

    from inspect import getsource
    source = (getsource(opt.__class__))
    print(source)


if __name__=='__main__':
    import fire
    fire.Fire()
