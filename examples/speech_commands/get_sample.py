import os, time, sys, platform

import numpy as np
import array, random
import glob
from scipy.io import wavfile

dataset_link = "https://storage.cloud.google.com/download.tensorflow.org/data/speech_commands_v0.01.tar.gz"

filedir = "D:\\speech_commands_v0.01/"
if platform.system().lower() != "windows":
	filedir = "/usr/local/speech_commands_v0.01/"

commands = ['yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off', 'stop', 'go']
for command in commands:
	if (os.path.exists(filedir + command)):
		continue
	print("Please download the speech commands dataset from " + dataset_link + " and extract it into " + filedir)
	os._exit(0)

random.seed(2)

X_SIZE = 16000

train_in_bytes = bytearray()
train_in_head = np.zeros(8).astype('int32')
train_in_head[1:4] = [X_SIZE, 1, 1]
train_in_bytes += train_in_head.tobytes()

train_out_bytes = bytearray()
train_out_head = np.zeros(8).astype('int32')
train_out_head[1:4] = [1, 1, 1]
train_out_bytes += train_out_head.tobytes()

test_in_bytes = bytearray()
test_in_bytes += train_in_head.tobytes()

test_out_bytes = bytearray()
test_out_bytes += train_out_head.tobytes()

Y = np.array([0]).astype('float32')

for (Y[0], command) in enumerate(commands):
	paths = glob.glob(filedir + command + '/*.wav')
	paths.sort()
	random.shuffle(paths)
	paths_len = len(paths)

	print(command, paths_len)

	for i in range(paths_len):
		framerate, wav_data = wavfile.read(paths[i])
		
		if len(wav_data) > X_SIZE:
			print("%d, %d" % (len(wav_data), X_SIZE))
			wav_data = wav_data[:X_SIZE]

		X = np.zeros(X_SIZE, dtype="float32")
		X[:len(wav_data)] += wav_data

		X = (X-X.min())/(X.max()-X.min()) 
		# X -= 0.5

		if i < paths_len * 0.9:
			train_in_bytes += X.tobytes()
			train_out_bytes += Y.tobytes()
		else:
			test_in_bytes += X.tobytes()
			test_out_bytes += Y.tobytes()

# import matplotlib.pyplot as plt
# plt.plot(X)
# plt.show()
# os._exit(0)

with open("train_in.smpl", "wb") as file:
	file.write(train_in_bytes)
with open("train_out.smpl", "wb") as file:
	file.write(train_out_bytes)

with open("test_in.smpl", "wb") as file:
	file.write(test_in_bytes)
with open("test_out.smpl", "wb") as file:
	file.write(test_out_bytes)









