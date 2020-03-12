import random
import numpy as np
import keras
from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Concatenate, Dot, Lambda, Input,Conv2D,MaxPool2D,Dropout
from keras.datasets import mnist
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from keras import backend as K
import os
import cv2
import glob
import pandas as pd
from sklearn.utils import shuffle

class PreProcess():
    def __init__(self,image_file_name):
        self.image_file_name = image_file_name
        self.data_frame=None
        self.label_mapping = self.genrate_mapping()
        
    def genrate_mapping(self):
        mapping={}
        for i,v in enumerate(os.listdir(self.image_file_name)):
            mapping[v]=i
        return mapping
    
    def get_image_file(self,size=64):
        root_file = os.path.abspath(self.image_file_name)
        list_of_file = os.listdir(self.image_file_name)
        df_img = []
        df_label = []
        for x in list_of_file:
            path = os.listdir(os.path.join(root_file,x))
            c=0
            for pt in path:
                img_path = os.path.join(root_file,os.path.join(x,pt))
                image = cv2.imread(img_path,0)
                image = cv2.resize(image,(size,size))
                df_img.append(list(image.reshape(1,-1)[0]))
                df_label.append(self.label_mapping[x])
                
                if(c==100):
                    break
                c+=1
                
        cvt_df={}
        col=0
        for i in range(len(df_img[0])):
            img_pixil_list=[]
            for j in range(len(df_img)):
                img_pixil_list.append(df_img[j][i])
            cvt_df["pixil"+str(col)]=img_pixil_list
            col+=1
            
        cvt_df['label'] = df_label
        self.data_frame= pd.DataFrame(cvt_df)
        self.data_frame = self.data_frame.sample(frac=1)
        return self.data_frame
    
    def save_minist_file(self):
        try:
            print("image converted")
            self.data_frame.to_csv("plant_minist.csv",index=False)
        except Exception as e:
            print("data not there")

class SiameseModel():
    def __init__(self,csv_file_name):
        self.csv_file_name = csv_file_name
        self.model = None
        self.pairs_train = None
        self.pairs_test = None
        self.labels_train = None
        self.labels_test = None
        self.y_pred=None
        
    def make_pairs(self,x, y):
        num_classes = max(y) + 1
        number_indices = [np.where(y == i)[0] for i in range(num_classes)]
        pairs = []
        labels = []

        for idx1 in range(len(x)):
            # add a matching example
            x1 = x[idx1]
            label1 = y[idx1]
            idx2 = random.choice(number_indices[label1])
            x2 = x[idx2]

            pairs += [[x1, x2]]
            labels += [1]

            # add a not matching example
            label2 = random.randint(0, num_classes-1)
            while label2 == label1:
                label2 = random.randint(0, num_classes-1)

            idx2 = random.choice(number_indices[label2])
            x2 = x[idx2]

            pairs += [[x1, x2]]
            labels += [0]
            for i in range(len(pairs)):
                for j in range(len(pairs[i])):
                    pairs[i][j] = pairs[i][j].reshape(64,64)
                    
        return np.array(pairs), np.array(labels)
    
    def train_model(self,epochs=10):
        try:
            self.model.fit([self.pairs_train[:,0], self.pairs_train[:,1]], self.labels_train[:], batch_size=16, epochs=epochs)
        except Exception as e:
            print("No Model Initialize")
            
    def predict_similarity(self):
        self.y_pred = self.model.predict([self.pairs_test[:,0],self.pairs_test[:,1]])
        return self.y_pred
    
    def euclidean_distance(self,vects):
        x, y = vects
        sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
        return K.sqrt(K.maximum(sum_square, K.epsilon()))
    
    def create_model(self,input_shape):
        i = input_shape[2]
        j = input_shape[3]
        inp = Input(shape=(i,j))
        x = Flatten()(inp)
        x = Dense(64, activation='relu')(x)
        x = Dropout(0.1)(x)
        x = Dense(128, activation='relu')(x)
        x = Dropout(0.1)(x)
        x = Dense(128, activation='relu')(x)
        x = Dropout(0.1)(x)
        x = Dense(256, activation='relu')(x)
        x = Dropout(0.1)(x)
        x = Dense(4096, activation='sigmoid')(x)
        dense = Model(inp, x)

        input1 = Input((i,j))
        input2 = Input((i,j))

        dense1 = dense(input1)
        dense2 = dense(input2)

        merge_layer = Lambda(self.euclidean_distance)([dense1,dense2])
        dense_layer = Dense(1, activation="sigmoid")(merge_layer)
        model = Model(inputs=[input1, input2], outputs=dense_layer)
        model.compile(loss = "binary_crossentropy", optimizer="adam", metrics=["accuracy"])
        return model
    
    def process_data(self):
        data = pd.read_csv(self.csv_file_name)
        labels = data['label'].values
        images = data.drop(['label'],axis=1).values
        x_train,x_test, y_train, y_test = train_test_split(images,labels,test_size=0.2,random_state=0)
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255
        self.pairs_train, self.labels_train = self.make_pairs(x_train, y_train)
        self.pairs_test, self.labels_test = self.make_pairs(x_test, y_test)
        self.model = self.create_model(self.pairs_train.shape)
        
    
if __name__ == "__main__":
    files = os.listdir()
    if("plant_minist.csv" not in files):
        model = PreProcess("PlantVillage")
        data = model.get_image_file()
        model.save_minist_file()
        sam = SiameseModel("plant_minist.csv")
        sam.process_data()
        sam.train_model(1)
        predictions=sam.predict_similarity()
        for i in range(len(predictions)):
            print("Pairs"+str(i)+" :",predictions[i])
    else:
        sam = SiameseModel("plant_minist.csv")
        sam.process_data()
        sam.train_model(1)
        predictions=sam.predict_similarity()
        for i in range(len(predictions)):
            print("Pairs"+str(i)+" :",predictions[i])