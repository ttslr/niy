import gzip
import os
import numpy as np
import struct
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

sample_in_bytes = bytearray()
sample_out_bytes = bytearray()
sample_in_head = np.zeros(8).astype("int32")
sample_out_head = np.zeros(8).astype("int32")

sample_in_head[1:4] = [1, 1, 1]
sample_out_head[1:4] = [128, 128, 3]

sample_in_bytes += sample_in_head.tobytes()
sample_out_bytes += sample_out_head.tobytes()

X = np.zeros(1).astype('float32')

filenames = ["files/girl.png", "files/sunflower.png"]
X[0] = 0
for filename in filenames:
	im = mpimg.imread(filename)
	im = im.transpose((2,0,1))

	im = im.astype("float32")

	if (im.max() - im.min()) <= 2:
		im *= 255.0
	im = im / 255.0 - 0.5

	print(filename, im.shape, im.dtype)	
	print(X[0], im.min(), im.max())	

	sample_in_bytes += X.tobytes()
	sample_out_bytes += im.tobytes()

	X[0] += 1

predict_in_bytes = bytearray()
predict_in_bytes += sample_in_head.tobytes()
X[0] = 0.5
predict_in_bytes += X.tobytes()

with open("train_in.smpl", "wb") as file:
	file.write(sample_in_bytes)

with open("train_out.smpl", "wb") as file:
	file.write(sample_out_bytes)

with open("predict_in.smpl", "wb") as file:
	file.write(predict_in_bytes)