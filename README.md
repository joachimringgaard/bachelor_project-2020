# bachelor_project-2020
My bachelor thesis and project revolving Convolutional Neural Networks (CNNs).

Deep Learning models are solving many of the problems that conventional machine learning and artificial intelligence have failed to solve previously. One of the methods used for deep learning is Convolutional Neural Networks (CNNs). CNNs are especially applied in image processing, both in the classification of images and in the detection of objects/structures in
images (e.g. detecting anomalies in medical images). The theory revolves around kernel convolutions that as input takes a sub-grid centered around a single pixel in the original full pixel grid, and does a weighted average of the sub-grid. This weighted average is the pixel intensity in the new (slightly smaller) convoluted pixel grid (due to loss of padding). This can be passed
to a polling layer tasked in finding the maximum or average of a small pixel grid (e.g. 3x3), which is passed on to the next layer. In this way you reduce the dimensions of the original image reducing the computational power needed in the fully connected neural network part of the CNN to come up with a classification/detection. There can be several convolutional
kernels and pooling layers that reduce dimensionality before the resulting matrix is flattened and passed to the neural network.

CNNs has been widely acknowledged due to their accurate results in image processing fields. This project will focus on the task of image classification through deep learning and especially CNNs. Different architectures of CNN will be implemented and tested on the same data set, to see differences in accuracy, confidence ratios on predictions and efficiency of the network.
The data set that the model is being trained and tested on will be fairly small as to accommodate the capabilities of a personal machine. This being said, the possibilities of using external computing resources, especially GPU power, will be explored as to speed up training and testing of the developed CNNs. One possible platform could be Google’s Collaboration
that offers the above mentioned. 

The project will include phases of empirical gathering, meaning understanding the theory
behind CNNs and related subjects. One of these could be the field of Adversarial Networks that seeks to correct the implications of Adversarial Attacks (AAs) on neural networks. AAs are small perturbations to images that remain imperceptible to human vision and that causes CNNs to wrongly predict classes for the given images with a high level of confidence. If the
scope of the project allows it, the implementation of the CNNs will try and include safety measures to detect and correct implications of AAs. Furhermore, implementations of different CNNs with different characteristics will be submitted including documentation of the networks and lastly a report will be written that analyzes and discusses the subject at hand
(this comprises the effect of AAs on modern day CNNs) and documents the developed CNNs - the bachelor report.
