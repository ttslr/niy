import gzip
import os
import numpy as np
import struct
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

filename = r"files/peach_blossom.jpg"

print(filename)

sample_in_bytes = bytearray()
sample_out_bytes = bytearray()
sample_in_head = np.zeros(8).astype("int32")
sample_out_head = np.zeros(8).astype("int32")

sample_in_head[1:4] = [1, 1, 2]
sample_out_head[1:4] = [1, 1, 3]

im = mpimg.imread(filename)

im = im[:,:,:3]
if im.shape[2] != 3:
	os._exit(0)

im = im.astype("float32")
if (im.max() - im.min()) <= 1:
	im *= 255.0
im = im / 255.0 - 0.5

XSIZE = im.shape[1]
YSIZE = im.shape[0]

print(XSIZE, YSIZE)	

sample_in_head[5:8] = [3, XSIZE, YSIZE]

sample_in_bytes += sample_in_head.tobytes()
sample_out_bytes += sample_out_head.tobytes()

ain = np.zeros(2).astype("float32")
aout = np.zeros(3).astype("float32")

for y in range(YSIZE):
	for x in range(XSIZE):
		ain[0] = (x - XSIZE // 2) / (XSIZE // 2)
		ain[1] = (y - YSIZE // 2) / (YSIZE // 2)
		aout = im[y][x]
		sample_in_bytes += ain.tobytes()
		sample_out_bytes += aout.tobytes()

with open("train_in.smpl", "wb") as file:
	file.write(sample_in_bytes)

with open("train_out.smpl", "wb") as file:
	file.write(sample_out_bytes)

im = mpimg.imread(filename)
plt.imshow(im)
plt.show()