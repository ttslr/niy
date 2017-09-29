Niy
====  
Deep Learning Framework By WILAB

| **`Windows`** |
|-------------|

Why Niy?
----
* Learn without writing any code
* Super easy
* Super mini
* Better performance over a variety of tasks

Supported Features
----
### Layers
* Convolution Layer
  * Grouped Convolution Layer
  * Dilated (Grouped) Convolution Layer
  * Locally Connected (Grouped) Convolution Layer
  * Locally Connected Dilated (Grouped) Convolution Layer
* Deconvolution Layer
  * Grouped Deconvolution Layer
  * Dilated (Grouped) Deconvolution Layer
  * Locally Connected (Grouped) Deconvolution Layer
  * Locally Connected Dilated (Grouped) Deconvolution Layer
* Pooling Layer
  * Max Pooling
  * Abs Max Pooling
  * Average Pooling
  * Random Pooling
* Merge Layer
* Dropout Layer
* Shortcut Layer

Try Now!
----
Let's take the famous mnist dataset as example
### Step 1: Define Your MODEL 
    # edit model.txt
    [
        {Shape: [28, 28, 1]},
        {Shape: [14, 14, 2], Kernel: [6, 6], Pad: [2, 2]},
        {Shape: [7, 7, 4], Kernel: [6, 6], Pad: [2, 2]},
        {Shape: [1, 1, 10], Kernel: [7, 7]},
    ]
    
### Step 2: Define Your CONF
    # edit conf.txt
    {
        Rate: 4e-2,
        LossType: 'softmax',
        EpochTrain: 2,
        
        Model: '_mnist/model.txt',
        TrainIn: '_mnist/train_in.saml',
        TrainOut: '_mnist/train_out.saml',
    }
    
### Step 3: Run
    # niy model.txt

### Finish
You will get a test accuracy around 98% after one or two minutes

Tutorial
----
There are four kinds of file
1. CONF
<br>　stores configuration information
2. MODEL
<br>　stores model information
3. SAMPLE
<br>　stores sample information
4. PARA
<br>　stores bias, weight, loss, rate... 

Niy uses [CON](https://github.com/microic/con) to define MODEL and CONF

### MODEL
| Name | Description | Default |
|--|--|--|
| Debug | **false**: do not show debug information<br>**true**: show debug information | true |
| Load | **0**: do not load<br>**1**: load bias and weight only<br>**2**: load all | 0 |
| Rate | initial learning rate | 0.02 |
| Decay | learning rate decay | 0.9 |
| InputType | **'pointwise'**<br>**'onehot'** | 'pointwise' |
| LossType | **'mse'**<br>**'softmax'**<br>**'max'** | 'mse' |
| EpochTrain | how many epochs to train | 1 |
| EpochDecay | how often to decay | 0.2 |
| EpochLog | how often to log | 0.2 |


License
----
Copyright 2017 WILAB

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

