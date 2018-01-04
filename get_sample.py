import gzip
import os
import numpy as np
import struct
import matplotlib.pyplot as plt

def get_sample_in(filename, des):
	sample_in_bytes = bytearray()
	sample_in_head = np.zeros(8).astype("int32")

	sample_in_head[1:4] = [28, 28, 1]

	sample_in_bytes += sample_in_head.tobytes()

	with gzip.open(filename , 'rb') as file:
		buf = file.read()
	 
	index = 0

	form = '>IIII'
	magic, numImages, numRows, numColumns = struct.unpack_from(form, buf, index)
	index += struct.calcsize(form)

	print("get_sample_in", filename)
	for i in range(numImages):
		form = '>784B'
		im_data = struct.unpack_from(form, buf, index)
		index += struct.calcsize(form)

		arr = np.array(im_data).astype("float32")
		arr = (arr - 128.0) / 128.0 
		sample_in_bytes += arr.tobytes()
		
		if i % 10000 == 0: print("", i)

	with open(des, "wb") as file:
		file.write(sample_in_bytes)

def get_sample_out(filename, des):
	sample_out_bytes = bytearray()
	sample_out_head = np.zeros(8).astype("int32")

	sample_out_head[1:4] = [1, 1, 1]

	sample_out_bytes += sample_out_head.tobytes()
	with gzip.open(filename , 'rb') as file:
		buf = file.read()

	index = 0
	form = '>II'
	magic, numItems = struct.unpack_from(form, buf, index)
	index += struct.calcsize(form)

	print("get_sample_out", filename)
	for i in range(numItems):
		form = '>1B'
		label_data = struct.unpack_from(form, buf, index)
		index += struct.calcsize(form)

		arr = np.array(label_data).astype("float32")
		sample_out_bytes += arr.tobytes()

	with open(des, "wb") as file:
		file.write(sample_out_bytes)

get_sample_in('files/train-images-idx3-ubyte.gz', "train_in.smpl")
get_sample_out("files/train-labels-idx1-ubyte.gz", "train_out.smpl")

get_sample_in('files/t10k-images-idx3-ubyte.gz', "test_in.smpl")
get_sample_out("files/t10k-labels-idx1-ubyte.gz", "test_out.smpl")