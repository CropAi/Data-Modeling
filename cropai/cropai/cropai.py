def cropai():
    import numpy as np
    import keras
    from keras.preprocessing.image import ImageDataGenerator
    from keras.layers.normalization import BatchNormalization
    from keras.layers.convolutional import *
    from sklearn.metrics import confusion_matrix
    from keras.preprocessing.image import img_to_array
    import itertools
    from IPython.display import display
    from PIL import Image
    import matplotlib.pyplot as plt
    import cv2
    import h5py


    path = '/Users/valdermaut/Downloads/PlantVillage/PlantVillage'
'


    batches = ImageDataGenerator().flow_from_directory(
        path,
        target_size=(224, 224),
        classes=[
            'Pepper__bell___Bacterial_spot',
            'Pepper__bell___healthy',
            'Potato___Early_blight',
            'Potato___healthy',
            'Potato___Late_blight',
            'Tomato_Bacterial_spot',
            'Tomato_Early_blight',
            'Tomato_healthy',
            'Tomato_Late_blight',
            'Tomato_Leaf_Mold',
            'Tomato_Septoria_leaf_spot',
            'Tomato_Spider_mites_Two_spotted_spider_mite',
            'Tomato__Target_Spot',
            'Tomato__Tomato_mosaic_virus',
            'Tomato__Tomato_YellowLeaf__Curl_Virus'
         ],
         batch_size=10
    )


    # plots images with labels within jupyter notebook
    def plots(ims, figsize=(12,6), rows=1, interp=False, titles=None):

        if type(ims[0]) is np.ndarray:
            ims = np.array(ims).astype(np.uint8)
            if (ims.shape[-1] != 3):
                ims = ims.transpose((0,2,3,1))
        f = plt.figure(figsize=figsize)
        cols = len(ims)//rows if len(ims) % 2 == 0 else len(ims)//rows + 1
        for i in range(len(ims)):
            sp = f.add_subplot(rows, cols, i+1)
            sp.axis('Off')
            if titles is not None:
                sp.set_title(titles[i], fontsize=16)
            plt.imshow(ims[i], interpolation=None if interp else 'none')


    imgs, labels = next(batches)
    plots(imgs, titles=labels)


    import cv2
    import glob

    files1 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Pepper__bell___Bacterial_spot/*.JPG")
    files2 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Pepper__bell___healthy/*.JPG")
    files3 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Potato___Early_blight/*.JPG") 
    files4 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Potato___healthy/*.JPG")
    files5 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Potato___Late_blight/*.JPG")
    files6 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_Bacterial_spot/*.JPG")
    files7 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_Early_blight/*.JPG")
    files8 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_healthy/*.JPG") 
    files9 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_Late_blight/*.JPG")
    files10 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_Leaf_Mold/*.JPG")
    files11 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_Septoria_leaf_spot/*.JPG")
    files12 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato_Spider_mites_Two_spotted_spider_mite/*.JPG")
    files13 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato__Target_Spot/*.JPG")
    files14 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato__Tomato_mosaic_virus/*.JPG")
    files15 = glob.glob ("/Users/valdermaut/Downloads/PlantVillage/PlantVillage/Tomato__Tomato_YellowLeaf__Curl_Virus/*.JPG")




    with h5py.File('/Users/valdermaut/Downloads/PlantVillage/PlantVillage/main.h5', 'a') as hdf:
        G = hdf.create_group('Group')
        X1_data=[]
        for myFile in files1:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G1 = hdf.create_group('G/Group1')
        G1.create_dataset('dataset1',data=X1_data)
        X1_data=[]
        for myFile in files2:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G2 = hdf.create_group('G/Group2')
        G2.create_dataset('dataset2',data=X1_data)
        X1_data=[]
        for myFile in files3:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G3 = hdf.create_group('G/Group3')
        G3.create_dataset('dataset3',data=X1_data)
        X1_data=[]
        for myFile in files4:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G4 = hdf.create_group('G/Group4')
        G4.create_dataset('dataset4',data=X1_data)
        X1_data=[]
        for myFile in files5:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G5 = hdf.create_group('G/Group5')
        G5.create_dataset('dataset5',data=X1_data)
        X1_data=[]
        for myFile in files6:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G6 = hdf.create_group('G/Group6')
        G6.create_dataset('dataset6',data=X1_data)
        X1_data=[]
        for myFile in files7:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G7 = hdf.create_group('G/Group7')
        G7.create_dataset('dataset7',data=X1_data)
        X1_data=[]
        for myFile in files8:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G8 = hdf.create_group('G/Group8')
        G8.create_dataset('dataset8',data=X1_data)
        X1_data=[]
        for myFile in files9:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G9 = hdf.create_group('G/Group9')
        G9.create_dataset('dataset9',data=X1_data)
        X1_data=[]
        for myFile in files10:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G10 = hdf.create_group('G/Group10')
        G10.create_dataset('dataset10',data=X1_data)
        X1_data=[]
        for myFile in files11:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G11 = hdf.create_group('G/Group11')
        G11.create_dataset('dataset11',data=X1_data)
        X1_data=[]
        for myFile in files12:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G12 = hdf.create_group('G/Group12')
        G12.create_dataset('dataset12',data=X1_data)
        X1_data=[]
        for myFile in files13:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G13 = hdf.create_group('G/Group13')
        G13.create_dataset('dataset13',data=X1_data)
        X1_data=[]
        for myFile in files14:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G14 = hdf.create_group('G/Group14')
        G14.create_dataset('dataset14',data=X1_data)
        X1_data=[]
        for myFile in files15:
            #print(myFile)
            image = cv2.imread (myFile)
            X1_data.append (image)
        X1_data=np.array(X1_data)
        G15 = hdf.create_group('G/Group15')
        G15.create_dataset('dataset15',data=X1_data)
