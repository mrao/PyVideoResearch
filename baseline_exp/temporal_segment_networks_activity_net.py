#!/usr/bin/env python
# Temporal Segment Networks on top of ResNet152 single frame model
# trained on ActivityNet
# Original name: anet1
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
    '--dataset', 'activitynet_tsn',
    '--arch', 'resnet152',
    '--wrapper', 'tsn_base2',
    '--criterion', 'default',
    '--temporal-segments', '3',
    '--lr', '0.01',
    '--lr-decay-rate', '50',
    '--epochs', '120',
    '--batch-size', '15',
    '--train-size', '0.1',
    '--weight-decay', '0.0001',
    '--window-smooth', '0',
    '--val-size', '0.1',
    '--cache-dir', '/nfs.yoda/gsigurds/ai2/caches/',
    '--data', '/scratch/gsigurds/activitynet_jpg4/',
    '--train-file', '/nfs.yoda/gsigurds/activity_net.v1-3.min.json',
    '--val-file', '/nfs.yoda/gsigurds/activity_net.v1-3.min.json',
    '--label-file', '/nfs.yoda/gsigurds/activity_net.v1-3.min.json',
    '--nclass', '200',
    '--pretrained',
    '--originalloss-weight', '1',
    '--resume', '/nfs.yoda/gsigurds/ai2/caches/' + __file__.split('/')[-1].split('.')[0] + '/model.pth.tar',
    #'--evaluate',
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
