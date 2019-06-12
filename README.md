# grabai_cv
Repository for Computer Vision problem of Grab-AI competition at https://www.aiforsea.com/computer-vision. The goal is to create an AI that is capable of automatically recognize the model and make of a car given the image.
To solve for this problem the approach used will be deep learning based model (InceptionV3 and SEResNet50), all of which build using Keras framework with Tensorflow as it's backend.

Several steps that are taken in order to fulfil the goal are as follow:

1. Data analysis
Checking the distribution of downloaded train and test data. Generate validation data. EDA of the data Using T-SNE.

2.Training Preparation
Preparing the callbacks and data generator for the model.

3.Model Benchmark
Creating base model benchmark that is not so complex and fast to train. InceptionV3 is used as the model benchmark.

4. Further Model
Two more complex model will be created for final comparison, both of which are based on SeResNet50. Final model perform at 71.316% accuracy with testing data.
