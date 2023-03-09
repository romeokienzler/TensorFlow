You can find the translation to Spanish below for a better undestanding
Enjoy!

############### English Version##########################################################################################################################
# What's new in TensorFlow 2.x

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



############################# SPANISH VERSION ###############################################################################

# Novedades en TensorFlow 2.x

Los siguientes son todos los cambios que vienen en TensorFlow 2.x. Echemos un vistazo más de cerca a ellos:

* Ejecución ansiosa / tf.function
* Integración de la API de Keras
* Capacitación distribuida facilitada
* Datos de TF
* Modelo guardado TF
* Centro TensorFlow
* Servicio de TensorFlow
* TensorFlow Lite
* TensorFlow.js
* Ordenar la API
* La herramienta de conversión
* Alcance variable alternativo
  

## Ejecución ansiosa


La falta de ejecución entusiasta fue una de las principales quejas contra TensorFlow. Todos podemos relacionarnos. Tener que ejecutar todo el gráfico y luego tratar de depurar en función de los errores fue muy tedioso. Especialmente, dado que los valores de los resultados intermedios no han sido accesibles sin imprimirlos mezclando declaraciones de depuración en el código de producción.

Con TensorFlow 2.0, la ejecución ansiosa está activada de manera predeterminada y lo mejor es que el código casi no cambia. Debajo del capó, solo está trabajando con los llamados "EagerTensors" en lugar de "Tensors", pero dado que comparten la misma interfaz, la diferencia apenas se nota. Incluso en la velocidad de ejecución, la diferencia es difícil de ver.

Esto significa que, de ahora en adelante, el código de TensorFlow se puede usar y depurar como un código de python normal (usando numpy, por ejemplo). Este es un aspecto de hacer que TensorFlow sea más pitónico.

A continuación hay dos tareas. Recomiendo encarecidamente hacerlos porque mientras me ves codificando y codificando tú mismo definitivamente interiorizarás el material.

### Tareas

1. [Mírame programar](https://www.youtube.com/watch?v=J3_b4461qxU)


2. [Codifíquese usted mismo](https://github.com/romeokienzler/TensorFlow/blob/master/notebooks/tf2.eagerexec.ipynb)

## Integración de la API de Keras

En realidad, Keras es una de las mejores API del planeta para DeepLearning. Ahora Keras ha sido devorado por TensorFlow. Un poco triste, pero en realidad no hace ninguna diferencia ya que casi todos usaron Keras además de TensorFlow de todos modos. Entonces, consideremos a Keras como parte de TensorFlow (o TensorFlow como parte de Keras). Lo bueno es que ahora puede usar la API Keras directa y fácil de usar y aún puede afirmar que es un desarrollador de TensorFlow. Sí, Google convirtió a Keras en la API oficial de alto nivel de TensorFlow.

Así que podrías pensar, ¿y qué? Solo cambian algunas importaciones. Pero esto es sólo una parte de la historia. Sí, las importaciones cambiaron y, como puede ver más adelante en el ejemplo, básicamente puede dejar intacto su código Keras existente la mayoría de las veces y simplemente cambiar la importación y listo.

Pero además, Keras ahora puede hacer uso de la funcionalidad integrada de TensorFlow que antes no era posible. Por ejemplo, puede tomar su código Keras 1:1 y TensorFlow lo escalará a un gran clúster de GPU o TPU. Echaremos un vistazo a esto en el próximo capítulo.

Por ahora, solo siga el video y el ejercicio de código a continuación para tener una idea de cómo funcionan las cosas:

### Tareas

1. [Mírame programar](https://www.youtube.com/watch?v=D4mJZQdgV0Y)


2. [Codifíquese usted mismo](https://github.com/romeokienzler/TensorFlow/blob/master/notebooks/tf2.keras.ipynb)



Si desea obtener más información, consulte nuestro [libro] (https://learning.oreilly.com/library/view/whats-new-in/9781492073727/)
