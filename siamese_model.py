def siamese_model(input_shape):
    
    '''
    This function builds a siamese model. It takes two input images and returns similarity score. 
    we find the feature vector for two input images using CNN and sqaush the final output.
    '''
    
    #Input images
    input_1 = Input(input_shape)
    input_2 = Input(input_shape)

    #Convolutional neural network
    model = Sequential()
    model.add(Conv2D(64, (10,10), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D())
    model.add(Conv2D(128, (7,7), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(128, (4,4), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(256, (4,4), activation='relu'))
    model.add(Flatten())
    model.add(Dense(4096, activation='sigmoid'))

    # Feature vector for input images
    # Using the same model to share the weights between input_images.
    out_1 = model(input_1)
    out_2 = model(input_2)
    
    #Creating a custom layer that finds the L2Norm between two vectors
    L2_layer = Lambda(lambda t: K.sqrt(K.sum(K.square(t[0] - t[1]), axis=-1 )))
    L2_distance = L2_layer([out_1, out_2])
    # Squashing the output layer by applying sigmoid activation function
    y_pred = Activation('sigmoid')(L2_distance)
    
    # Final Siamese model
    siamese_model = Model(inputs=[input_1,input_2],outputs=y_pred)

    return siamese_model
    
