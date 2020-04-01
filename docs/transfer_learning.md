
# TRANSFER LEARNING FOR CROP DISEASE DETECTION

Transfer learning is not a machine learning model or technique; it is rather a 'design methodology' within machine learning. The main idea behind transfer learning is to borrow labeled data or extract knowledge from some related domains to help a machine learning algorithm to achieve greater performance in the domain of interest. This is very useful since most real-world problems typically do not have millions of labeled data points to train complex models and also it reduces training time.

It is a popular approach in deep learning where pre-trained models developed for a task is reused as the starting point for a model on a second task as the starting point.

## WHEN TO USE TRANSFER LEARNING

As is always the case in machine learning, it is hard to form rules that are generally applicable, but transfer learning might be used:

1. There isn't enough labeled training data to train your network from scratch.
2. There already exists a network that is pre-trained on a similar task, which is usually trained on massive amounts of data.
3. When task 1 and task 2 have the same input.

Transfer learning only works if the features learned from the first task are general, meaning they can be useful for another related task as well. Also, the input of the model needs to have the same size as it was initially trained with. If you don’t have that, add a pre-processing step to resize your input to the needed size.

## WHY TRANSFER LEARNING?

1. In practice a very few people train a Convolution network from scratch (random initialisation) because it is rare to get enough dataset. So, using pre-trained network weights as initialisations or a fixed feature extractor helps in solving most of the problems in hand.
2. Deep Networks are expensive to train. The most complex models take weeks to train using hundreds of machines equipped with expensive GPUs.
3. Determining the topology/flavour/training method/hyper parameters for deep learning is a black art with not much theory to guide.

## APPROACHES TO TRANSFER LEARNING USING A PRE-TRAINED MODEL
In computer vision, for example, neural networks usually try to detect edges in the earlier layers, shapes in the middle layer and some task-specific features in the later layers. In transfer learning, the early and middle layers are used and we only retrain the latter layers. It helps leverage the labeled data of the task it was initially trained on. 

The API of Keras allows you to load pre-trained networks and keep several of the layers fixed during training. Some state of the art pre-trained machine learning models are Alexnet, VGG, Inception, ResNet and mobilenet. These neural networks are very deep and contains millions of parameters. The large number of parameters allow to learn more complex patterns and therfore achieve higher accuracies. However, large number of parameters would take large amount of time to train and will use lot of memory. 

Mobilenet trained on ImageNet dataset could be used for the problem in hand as it uses an efficient neural network architecture that minimizes the amount of memory required and is used for various mobile applications.

## Steps

1. Select a pre-trained model from tensorflow-keras library.: TensorFlow Hub is an online repository of already trained TensorFlow models that can be used. In addition to complete models, TensorFlow Hub also distributes models without the last classification layer. These can be used to easily do transfer learning. 
```
IMAGE_RES=224//This would be depend on model. Mobilenet takes image of sixe 224*224
URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/2"
feature_extractor = hub.KerasLayer(URL, input_shape=(IMAGE_RES, IMAGE_RES,3))
```

2. Pre-Process data/image size same as that expected by the model selected

3. Freeze the convolutional layers:  Freeze the variables in the feature extractor layer, so that the training only modifies the final classifier layer. By Freezing, only the variables of the last classification layer get trained and variables from other layers of pre-trained model are kept the same. This also reduces the training time significantly.

```
feature_extractor.trainable = False
```

4. Attach a classification head:  Now wrap the hub layer in a tf.keras.Sequential model, and add a new classification layer. Change the output classifier based on number of outputs expected.

```
model = tf.keras.Sequential([feature_extractor, layers.Dense(X)]) // X will be equal to number of output of our problem. By deffault imagenet has 1000 outputs
model.summary()
```

5. Train the model: Now train this model like any other, by first calling compile followed by fit.
```
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
history = model.fit(train_batches, epochs=EPOCHS, validation_data=validation_batches)
```

6. Make prediction and check Accuracy



**References**

1. https://towardsdatascience.com/transfer-learning-from-pre-trained-models-f2393f124751
2. https://keras.io/applications/
3. https://www.ntu.edu.sg/home/sinnopan/publications/[BookChapter14]Transfer%20Learning.pdf
4. https://www.datacamp.com/community/tutorials/transfer-learning
5. https://builtin.com/data-science/transfer-learning
6. https://medium.com/@14prakash/transfer-learning-using-keras-d804b2e04ef8




