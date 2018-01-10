[Niy](https://github.com/microic/niy)
====
A super mini but powerful deep learning framework written in pure c language

| **`Windows`** | **`Linux`** |
|-------------|-------------|

Sponsor Is Welcome
----
We need sponsorship to develop Niy<br>

Sponsor will get the following rights:
* Rename Niy
* Get a copy of Niy's source code
* Decide whether or not to make Niy open source

The sponsorship will be used on developing Niy and nothing else

Installation
----
Select one of the following experiments
* [image painting](https://github.com/microic/niy/tree/image_painting)
* [mnist](https://github.com/microic/niy/tree/mnist)
* [cifar10](https://github.com/microic/niy/tree/cifar10)

Or try some funny [examples](https://github.com/microic/niy/tree/master/examples/)

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

Example
----
Let's take the famous mnist dataset as example
### Step 1: Edit model file 
    # model.txt
    [
        {Shape: [28, 28, 1]},
        {Shape: [14, 14, 2], Kernel: [6, 6], Pad: [2, 2]},
        {Shape: [7, 7, 4], Kernel: [6, 6], Pad: [2, 2]},
        {Shape: [1, 1, 10], Kernel: [7, 7]},
    ]
    
### Step 2: Edit conf file 
    # conf.txt
    {
        Load: 0,
        
        RateInit: 0.01,

        EpochTrain: 3,
        EpochDecay: 0.2,
        EpochLog: 0.2,

        InputType: 'pointwise',
        LossType: 'softmax',

        Image: {
          Draw: true,
          Src: 'layer 0',
        },

        FreqTest: 2,
    }
    
### Step 3: Run
    # niy conf.txt

You will get a test accuracy around 98% after one or two minutes

Tutorial
----
There are four kinds of file
1. Model
<br>　Stores model information
2. Conf
<br>　Stores configuration information
3. Sample
<br>　Stores sample data
4. Para
<br>　Stores biases, weights, loss, rate... 

Niy uses [CON](https://github.com/microic/con) to define model and conf files

### Model
| Name | Description | Default |
|--|--|--|
| Shape | layer shape | [0, 0, 0] |
| Reshape | change the layer shape when output | null |
| Kernel | kernel size | [0, 0] |
| Dilation | dilate the kernel | 1 |
| Pad | padding | [0, 0] |
| PoolType | **'max'**<br>**'ave'**<br>**'amax'**: absolute maximum<br>**'rand'** | 'ave' |
| IsLocal | switch to locally connected layer | false |
| IsReverse | switch to deconvolution layer<br>*deconvolution means the reverse operation of convolution here, not transpose convolution* | false |
| IsMerge | switch to merge layer | 1 |
| Group | split the channels into groups | 1 |
| Dropout | dropout | null |
| Shortcut | shortcut to one top layer | null |

### Conf
| Name | Description | Default |
|--|--|--|
| Debug | show debug information or not | true |
| Load | **0**: do not load<br>**1**: load biases and weights only<br>**2**: load all | 0 |
| RateInit | initial learning rate | 0.02 |
| RateDecay | learning rate decay | 0.9 |
| InputType | **'pointwise'**<br>**'onehot'** | 'pointwise' |
| LossType | **'mse'**<br>**'softmax'**<br>**'max'**<br>**'zero'** | 'mse' |
| LossInit |  initial loss | 5 |
| LossMul | used to calculate the moving average of loss | 0.001 |
| Regularization | used to limit bias/weight | 1 |
| BiasFiller.Type | 'zero', 'uniform', 'usni', 'usno', 'usnio', 'usnf', 'gaussian', 'gsni', 'gsno', 'gsnio', 'gsnf' | 'zero'<br>
> u means uniform
 s mean sqrt |
| BiasFiller.Adj | used to adjust initial bias value<br><i>new = (old + adj[0])*adj[1]</i> | [0, 1] |
| WeightFiller.Type | 'zero', 'uniform', 'usni', 'usno', 'usnio', 'usnf', 'gaussian', 'gsni', 'gsno', 'gsnio', 'gsnf' | 'gsni' |
| WeightFiller.Adj | used to adjust initial weight value<br><i>new = (old + adj[0])*adj[1]</i> | [0, 0.8] |
| Image.Draw | draw current image or not | false |
| Image.Adj | used to adjust pixel value<br><i>new = (old + adj[0])*adj[1]</i> | [0.5, 255] |
| Image.Src | **'layer 0'**<br>**'layer last'**<br>**'predict'** | 'layer 0' |
| Image.Path | image file path | '_img.bmp' |
| Model | model file path | 'model.txt' |
| Para | para file path | 'para.bin' |
| TrainIn | train input sample file path | 'train_in.smpl' |
| TrainOut | train output sample file path | 'train_out.smpl' |
| TestIn | test input sample file path | 'test_in.smpl' |
| TestOut | test output sample file path | 'test_out.smpl' |
| PredictIn | predict input sample file path | 'predict_in.smpl' |
| PredictOut | predict output sample file path | 'predict_out.smpl' |
| EpochTrain | how many epochs to train | 1 |
| EpochDecay | how often to decay | 0.2 |
| EpochLog | how often to log | 0.2 |
| FreqTest | the frequency to test<br>**0**: never<br>**1**: test after training<br>**2**: test at each log time | 0 |
| FreqPredict | the frequency to predict<br>**0**: never<br>**1**: predict after training<br>**2**: predict at each log time | 0 |
| FreqSave | the frequency to save<br>**0**: never<br>**1**: save after training<br>**2**: save at each log time | 0 |
| TestTable | test table size | 0 |
| PredictTable | predict table size | 0 |

### Sample
| Address | Datatype | Description |
|--|--|--|
| 0 | int32 | set to zero |
| 4 | int32 | sample shape X-axis |
| 8 | int32 | sample shape Y-axis |
| 12 | int32 | sample shape Z-axis |
| 16 | int32 | number of samples<br>if set to zero, the program will calculate automatically |
| 20 | int32 | image shape X-axis<br>set to zero if not used |
| 24 | int32 | image shape Y-axis<br>set to zero if not used |
| 28 | int32 | image shape Z-axis<br>set to zero if not used |
| 32 | float32 array | sample data |

TODO
----
* Support GPU
* Support Intel MKL

