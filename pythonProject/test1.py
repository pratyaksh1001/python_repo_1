from gtts import gTTS
import os
mytext = ''''
The core data structures of Keras are layers and models. A layer is a simple input/output transformation, and a model is a directed acyclic graph (DAG) of layers.

Layers
The tf.keras.layers.Layer class is the fundamental abstraction in Keras. A Layer encapsulates a state (weights) and some computation (defined in the tf.keras.layers.Layer.call method).

Weights created by layers can be trainable or non-trainable. Layers are recursively composable: If you assign a layer instance as an attribute of another layer, the outer layer will start tracking the weights created by the inner layer.

You can also use layers to handle data preprocessing tasks like normalization and text vectorization. Preprocessing layers can be included directly into a model, either during or after training, which makes the model portable.
'''
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
