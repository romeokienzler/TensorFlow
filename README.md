# What's New in TensorFlow 2.x

The following are all the changes coming in TensorFlow 2.x. Let's have a closer look at them:

* Eager Execution / tf.function
* Integration of the Keras API
* Facilitated distributed training
* TF Data
* TF SavedModel
* TensorFlow Hub
* TensorFlow Serving
* TensorFlow Lite
* TensorFlow.js
* Tidying up the API
* The conversion tool
* Alternative variable scoping
  

## Eager Execution


Lack of eager execution was one of the main complaints against TensorFlow. We all can relate. Having to execute the whole graph and then trying to debug based on the errors was very tedious. Especially, since values of intermediate results haven't been accessible without printing them out by mixing in debug statements into the production code.

With TensorFlow 2.0, eager execution is activated by default and the very cool thing is that the code nearly doesn't change. Under the hood, you are just working with so-called "EagerTensors" instead of "Tensors" but since they share the same interface, the difference is barely noticeable. Even in execution speed, the difference is hard to see. 

This means, from now on, TensorFlow code can be used and debugged as ordinary python code (using numpy for example). This is one aspect of making TensorFlow more pythonic.

Below there are two tasks. I highly recommend doing them because while watching me coding and coding yourself you'll definitely internalize the material.

### Tasks

1. [Watch me coding](https://www.youtube.com/watch?v=J3_b4461qxU)


2. [Code yourself](https://github.com/romeokienzler/TensorFlow/blob/master/notebooks/tf2.eagerexec.ipynb) 

## Integration of the Keras API

Actually, Keras is one of the greatest APIs on the planet for DeepLearning. Now Keras has been eaten up by TensorFlow. A bit sad, but in reality it doesn't make any difference since nearly everyone used Keras on top of TensorFlow anyway. So let's consider Keras to be part of TensorFlow (or TensorFlow to be part of Keras). The cool thing is, that you now can use the straightforward, and easy to use Keras API and still can claim to be a TensorFlow developer. Yeah, Google made Keras the official high level API of TensorFlow.

So you might think, so what? Just some imports change. But this is only one part of the story. Yes, the imports changed, and as you can see later in the example, you can basically leave your existing Keras code intact most of the times and just change the import and you are done.

But in addition, Keras now can make use of built-in TensorFlow functionality which wasn't possible before. For example, you can take your 1:1 Keras code and TensorFlow will scale it to a large GPU or TPU cluster. We'll have a look at this in the next chapter.

For now, just follow along the video and code exercise below to get an idea how things work:

### Tasks

1. [Watch me coding](https://www.youtube.com/watch?v=D4mJZQdgV0Y)


2. [Code yourself](https://github.com/romeokienzler/TensorFlow/blob/master/notebooks/tf2.keras.ipynb) 



If you want to learn more, please have a look at our [book](https://learning.oreilly.com/library/view/whats-new-in/9781492073727/)

