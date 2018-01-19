Audio Recognition Using Spectrogram As Input 
====

By using spectrogram, we can simply treat audio recognition as image recognition. So all the technologies used at image recognition can be used at audio recognition as well

First, transform the original audio files into spectrograms, for example, the spectrogram for [test.wav](test.wav) is:
<img src="files/spectrogram.png" />

The samples used here is the same as [speech_commands](../speech_commands/)
To reduce the amount of computation, we limit the size of spectrogram to 128×128

Reference
----
* [Simple Audio Recognition](https://www.tensorflow.org/versions/master/