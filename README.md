# What's new in TensorFlow 2.0

The following are all the changes coming in TensorFlow 2.0. Let's have a closer look at them:

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



