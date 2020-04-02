from google_drive_downloader import GoogleDriveDownloader as gdd
from urllib.request import urlopen
import pickle
from tensorflow.keras.models import load_model 
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
import os
import numpy as np

class Model():
    """
        model_path{{string}}: path where model will be saved
        model{{string}}: deep learning model
        encoder{{string}}: load all the encoded file from encoder
    """
    def __init__(self, model_path ='./model.h5', encoder_path = 'encoder.pkl'):
        self.model_path = model_path
        gdd.download_file_from_google_drive(file_id='1Ssd4N2SWkro87azRHjObedqOTbxZ7dZ6',
                                            dest_path=model_path,
                                            unzip=True)
        self.model = load_model(model_path)
        self.model.summary
        self.encoder = pickle.load(open(encoder_path, 'rb'))
        
    def download_model(self, model_url = 'https://drive.google.com/open?id=1Ssd4N2SWkro87azRHjObedqOTbxZ7dZ6'):
        response = urlopen(model_url)
        html = load_model(response.read())
        return html
            
        """
            function is used to get path of saved model and if not present, return empty string
        """
    def getModel(self):
        try:
            if(os.path.exists(self.model_path)==True):
                path = os.path.abspath(self.model_path)
                return path
            else:
                print("Model not present")
                print("Download file first")
                return ""
        except Execption as e:
            print("Model not present")
            print("Download file first")
            return ""
			
    def predict_image(self, img_path):
      img = image.load_img(img_path, target_size=(256, 256))
      img_array = img_to_array(img) # Convert the images into NumPy array.
      img_array = np.expand_dims(img_array, axis=0)
      predictions = self.model.predict(img_array)
      index = np.flip(np.argsort(predictions[0])) # Sort the predictions in descending order.

      number_to_label = ['Tomato__Target_Spot', 'Tomato_Septoria_leaf_spot', 'Pepper__bell___Bacterial_spot', 'Tomato_healthy', 'Tomato_Early_blight', 'Potato___Late_blight', 'Potato___Early_blight', 'Pepper__bell___healthy', 'Tomato_Leaf_Mold', 'Tomato_Bacterial_spot', 
                         'Tomato__Tomato_mosaic_virus', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Late_blight', 'Potato___healthy']

      return (number_to_label[index[0]])


#if __name__ == "__main__":
#    img_file = sys.argv[1]
#    md = Model()
#    md.download_model()
#    print(md.getModel())
#    print(md)
#    result = md.predict_image(img_file)
#    print(result)