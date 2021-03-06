#!/usr/bin/env python
# Temporal Segment Network on top of ResNet152
# trained on Charades
# orignal name: trn2f3b
# model_best.txt:
#     loss_train 0.355067095641
#     loss_val 0.736642408198
#     mAP 0.251473939639
#     top1train 39.8389914989
#     top1val 43.6392901547
#     top5train 118.068847672
#     top5val 149.490065656
#     videoprec1 56.4680633545
#     videoprec5 198.872787476
import sys
import pdb
import traceback
sys.path.insert(0, '.')
from main import main
from bdb import BdbQuit
import os
os.nice(19)
import subprocess
subprocess.Popen('find ./exp/.. -iname "*.pyc" -delete'.split())

args = [
    '--name', __file__.split('/')[-1].split('.')[0],  # name is filename
    '--print-freq', '1',
    '--dataset', 'charades_tsn',
    '--arch', 'resnet152',
    '--wrapper', 'tsn_base2',
    '--criterion', 'default',
    '--temporal-segments', '3',
    '--lr', '2.5e-3',
    '--lr-decay-rate', '4',
    '--epochs', '20',
    '--batch-size', '15',
    '--train-size', '20.0',
    '--weight-decay', '0.0000001',
    '--window-smooth', '0',
    '--val-size', '1.0',
    '--cache-dir', '/nfs.yoda/gsigurds/ai2/caches/',
    '--data', '/scratch/gsigurds/Charades_v1_rgb/',
    '--train-file', '/home/gsigurds/ai2/twostream/Charades_v1_train.csv',
    '--val-file', '/home/gsigurds/ai2/twostream/Charades_v1_test.csv',
    '--pretrained',
    '--nhidden', '3',
    '--originalloss-weight', '5',
    '--resume', '/nfs.yoda/gsigurds/ai2/caches/' + __file__.split('/')[-1].split('.')[0] + '/model.pth.tar',
    '--workers', '4',
]
sys.argv.extend(args)
try:
    main()
except BdbQuit:
    sys.exit(1)
except Exception:
    traceback.print_exc()
    print('')
    pdb.post_mortem()
    sys.exit(1)
