Audio Recognition Using Spectrogram As Input 
====

By using spectrogram, we can simply treat audio recognition as image recognition, so all the technologies used at image recognition can be used at audio recognition as well

This example uses the same samples as [speech_commands](../speech_commands/), that is wave audio files of people saying ten different words('yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off', 'stop', 'go') from [Speech Commands dataset](https://storage.cloud.google.com/download.tensorflow.org/data/speech_commands_v0.01.tar.gz)

First, transform the original audio files into spectrograms, for example, the spectrogram for [test.wav](files/test.wav) is:
<div><img src="files/spectrogram.png" /></div>
The energy level is: Red > Green > Blue > Black(no energy)<br><br>

To reduce the amount of computation, we limit the size of spectrogram to 128×128, so the model can be defined as follow:
<div><img src="files/model.png" /></div> 

Run this model, you will get a test accuracy around 92% after 50 minutes


Reference
----
* [Simple Audio Recognition](https://www.tensorflow.org/versions/master/tutorials/audio_recognition)









