# coding: utf8
import torch
import warnings

class DefaultConfig(object):
   model = 'MyMobilenet' # 使用的模型，名字必须与models/__init__.py中的名字一致
   env = model #
   ATTACK = 1
   GENUINE = 0
   # train_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset/colored','/home/shashank/Desktop/Fingerprint/dataset/colored/BiometrikaTrain/Livetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset/colored','/home/shashank/Desktop/Fingerprint/dataset/colored/BiometrikaTrain/Spooftest.txt',ATTACK]
   #  ]
   # test_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset/colored','/home/shashank/Desktop/Fingerprint/dataset/colored/BiometrikaTest/Livetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset/colored','/home/shashank/Desktop/Fingerprint/dataset/colored/BiometrikaTest/Spooftest.txt',ATTACK]
   #  ]

   # train_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/BiometrikaTrain/Livetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/BiometrikaTrain/Spooftest.txt',ATTACK]
   #  ]
   # test_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/BiometrikaTest/Livetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/BiometrikaTest/Spooftest.txt',ATTACK]
   #  ]

   #GRAY
   # train_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/gray/train/alivetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/gray/train/faketest.txt',ATTACK]
   #  ]
   # test_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/gray/Test/alivetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/gray/Test/faketest.txt',ATTACK]
   #  ]


   #CrossMatch
   # train_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/CrossMatch/Training/Livetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/CrossMatch/Training/Faketest.txt',ATTACK]
   #  ]
   # test_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/CrossMatch/Testing/Livetest.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/CrossMatch/Testing/Faketest.txt',ATTACK]
   #  ]
   
   #resized
   #/home/shashank/Desktop/Fingerprint/dataset
   # train_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/1test.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/1test.txt',ATTACK]
   #  ]
   # test_filelists=[
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/1test.txt',GENUINE],
   #  ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/1test.txt',ATTACK]
   #  ]

   #ultimate
   train_filelists=[
    ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/ultimate/Train/Livetest.txt',GENUINE],
    ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/ultimate/Train/Spooftest.txt',ATTACK]
    ]
   test_filelists=[
    ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/ultimate/Test/Livetest.txt',GENUINE],
    ['/home/shashank/Desktop/Fingerprint/dataset','/home/shashank/Desktop/Fingerprint/dataset/ultimate/Test/Spooftest.txt',ATTACK]
    ]

   #load_model_path = 'checkpoints/model.pth' # 加载预训练的模型的路径，为None代表不加载
   load_model_path = None # 加载预训练的模型的路径，为None代表不加载

   batch_size = 8# batch size
   use_gpu = torch.cuda.is_available() # use GPU or not
   #use_gpu = True # use GPU or not
   num_workers = 8 # how many workers for loading data
   print_freq = 20 # print info every N batch
   debug_file = '/tmp/debug' # if os.path.exists(debug_file): enter ipdb
   result_name = 'result'

   max_epoch = 5
   lr = 0.01 # initial learning rate
   lr_decay = 0.5 # when val_loss increase, lr = lr*lr_decay
   lr_stepsize=3#learning step size
   weight_decay = 1e-5 # 损失函数
   cropscale = 3.5
   image_size = 224
def parse(self, kwargs):
   '''
   根据字典kwargs 更新 config参数
   '''
   # 更新配置参数
   for k, v in kwargs.items():
      if not hasattr(self, k):
          # 警告还是报错，取决于你个人的喜好
          warnings.warn("Warning: opt has not attribut %s" %k)
      setattr(self, k, v)

   # 打印配置信息
   print('user config:')
   for k, v in self.__class__.__dict__.items():
      if not k.startswith('__'):
          print(k, getattr(self, k))

DefaultConfig.parse = parse
opt = DefaultConfig()
