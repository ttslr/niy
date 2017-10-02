import pickle, gzip
import os, random

import numpy as np
import struct
import matplotlib.pyplot as plt

sample_in_bytes = bytearray()
sample_in_head = np.zeros(8).astype('int32')
sample_in_head[1:4] = [32, 32, 3]
sample_in_bytes += sample_in_head.tobytes()

sample_out_bytes = bytearray()
sample_out_head = np.zeros(8).astype('int32')
sample_out_head[1:4] = [1, 1, 1]
sample_out_bytes += sample_out_head.tobytes()

def add_data_batch(path):
	global sample_in_bytes
	global sample_out_bytes

	with open(path, 'rb') as file:
		data_batch = pickle.load(file, encoding='bytes')

	print(path, len(data_batch[b'data']))

	Y = np.zeros(1).astype('float32')
	for label in data_batch[b'labels']:
		Y[0] = label
		sample_out_bytes += Y.tobytes()

	for im_data in data_batch[b'data']:
		im = im_data.astype('float32')
		
		im = (im - im.min()) / (im.max() - im.min()) - 0.5
		sample_in_bytes += im.tobytes()

add_data_batch('src/data_batch_1')
add_data_batch('src/data_batch_2')
add_data_batch('src/data_batch_3')
add_data_batch('src/data_batch_4')
add_data_batch('src/data_batch_5')

with open("train_in.smpl", "wb") as file:
	file.write(sample_in_bytes)
with open("train_out.smpl", "wb") as file:
	file.write(sample_out_bytes)

sample_in_bytes = bytearray()
sample_in_head = np.zeros(8).astype('int32')
sample_in_head[1:4] = [32, 32, 3]
sample_in_bytes += sample_in_head.tobytes()

sample_out_bytes = bytearray()
sample_out_head = np.zeros(8).astype('int32')
sample_out_head[1:4] = [1, 1, 1]
sample_out_bytes += sample_out_head.tobytes()

add_data_batch('src/test_batch')

with open("test_in.smpl", "wb") as file:
	file.write(sample_in_bytes)
with open("test_out.smpl", "wb") as file:
	file.write(sample_out_bytes)