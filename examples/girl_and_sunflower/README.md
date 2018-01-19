A Simple Example To Learn Deconvolution And Locally Connected Deconvolution
====

Deconvolution means the reverse operation of convolution here, not transpose convolution

In this example, we will test two networks(Model A and Model B), Model B is similar to Model A except that Model B uses locally connected deconvolution
<div><b>Model A</b><br><img src="files/model_a.png" max-width="500px" /></div>
<div><b>Model B</b><br><img src="files/model_b.png" max-width="500px" /></div>

To make things as simple as possible, we use only the following two samples to train the network
<table><tr><td><img src="files/girl.png" max-width="500px" /></td><td><img src="files/sunflower.png" max-width="500px" /></td></tr></table>
If input is "0", output will be the photo of girl, if input is "1", output will be the photo of sunflower

After training, the network will remember the two photos

The question is, what will the output be if input is "0.2", "0.5" or "0.8"?

Why Model A and Model B have different outputs?


If f(0) = the photo of girl, f(1) = the photo of sunflower<br>
Model A thinks the following picture is f(0.5):
<div><img src="files/_img_a.png" max-width="500px" /></div>


Model B tends not to forget anything and is hard to remember anything as well<br>
The following picture is outputed by Model B:
<div><img src="files/_img_b.png" max-width="500px" /></div>



