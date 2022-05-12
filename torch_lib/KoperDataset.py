import cv2
import numpy as np
import os
import random

import torch
from torchvision import transforms
from torch.utils import data

import math



def compute_projection(tc_homo, intrinsic):
	print(tc_homo, intrinsic)


class Dataset(data.Dataset):

	def __init__(self, path, bins=2, overlap=0.1):
		self.dataset_path = '/home/hpahadia_3/Documents/3ddeepbox/code/3D-BoundingBox/koperData.pickle'
		self.top_calib_path = '/home/hpahadia_3/Documents/3ddeepbox/code/3D-BoundingBox/kopercalib.pickle'
		self.cam_calib_path = '/home/hpahadia_3/Documents/3ddeepbox/code/3D-BoundingBox/kopercameracalib.pickle'
		self.dataset = None
		self.calib = None
		self.cam_calib = None

		# read
		with open(self.dataset_path,'rb') as handle:
			self.dataset = pickle.load(handle)
		
		with open(self.top_calib_path,'rb') as handle:
			self.calib = pickle.load(handle)

		with open(self.cam_calib_path,'rb') as handle:
			self.cam_calib = pickle.load(handle)

		self.key = 'CALIB_SK_1'
		tc_homo = self.calib[key]['Tc_homo']
		cvc1 = self.camcalib[key]
		intrinsic = np.array(
						[[cvc1['fc'][0][0], 0, cvc1['cc'][0][0]],
						[0, cvc1['fc'][1][0], cvc1['cc'][1][0]],
						[0,            0,            1]])

		self.proj_matrix = compute_projection(tc_homo, intrinsic)

		self.bins = bins
		self.angle_bins = np.zeros(bins)
		self.interval = 2 * np.pi / bins

		for i in range(1,bins):
			self.angle_bins[i] = i * self.interval
		self.angle_bins += self.interval / 2 # center of the bin

		self.overlap = overlap

		# ranges for confidence
		# [(min angle in bin, max angle in bin), ... ]
		self.bin_ranges = []
		for i in range(0,bins):
			self.bin_ranges.append(( (i*self.interval - overlap) % (2*np.pi), \
								(i*self.interval + self.interval + overlap) % (2*np.pi)) )
		# hold average dimensions
		class_list = ['Car', 'Trucks', 'Pedestrians','Bikes','Misc']
		self.averages = ClassAverages(class_list)
