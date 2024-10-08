import torch
from torchvision import datasets,transforms
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import random

def load_dataset(args):
    if args.dataset == 'CIFAR100':
        from data import CIFAR100 as dataset
    elif args.dataset == 'PMNIST':
        from data import PMNIST as dataset
    elif args.dataset == 'CIFAR10':
        from data import CIFAR10 as dataset
    elif args.dataset == 'CIFAR10_label':
        from data import CIFAR10_label as dataset
    elif args.dataset == 'CIFAR10_Label15':
        from data import CIFAR10_Label15 as dataset
    elif args.dataset == 'SplitMNIST':
        from data import SplitMNIST as dataset
    elif args.dataset == 'SplitMNIST_label':
        from data import SplitMNIST_label as dataset
    elif args.dataset == 'CIFAR10_gauss':
        from data import CIFAR10_gauss as dataset
    elif args.dataset == 'mixture':
        from data import mixture as dataset
    else:
        raise(args.dataset + ' not supported.')

    data,taskcla,size = dataset.get(args)

    return data,taskcla,size



