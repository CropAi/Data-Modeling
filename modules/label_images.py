from google_drive_downloader import GoogleDriveDownloader as gdd
import urllib2
import pickle
from keras.model import load_model 
import os
# https://drive.google.com/open?id=1PwifTMRZxzIbl-yDlR9cCVZrNxYg1JNd

class Model():
    """
        model_path{{string}}: path where model will be saved
        model{{string}}: deep learning model
        encoder{{string}}: load all the encoded file from encoder
    """
    def __init__(self, model_path ='./model.h5', encoder_path = 'encoder.pkl'):
        self.model_path = model_path
        gdd.download_file_from_google_drive(file_id='1642JgezyxVSlowH9kiTuB6xCWr6KleEb',
                                            dest_path=model_path,
                                            unzip=True)
        self.model = load_model(model_path)
        self.encoder = pickle.load(open(encoder_path, 'rb'))
        
    def download_model(self, model_url = 'https://drive.google.com/file/d/1642JgezyxVSlowH9kiTuB6xCWr6KleEb/view?usp=sharing'):
        response = urllib2.urlopen(model_url)
        html = load_model(response.read())
        return html
            
        """
            function is used to get path of saved model and if not present, return empty string
        """
    def getModel(self):
        try:
            if(os.path.exists(self.self.model_path)==True):
                path = os.path.abspath(self.self.model_path)
                return path
            else:
                print("Model not present")
                print("Download file first")
                return ""
        except Execption as e:
            print("Model not present")
            print("Download file first")
            return ""
			
# if __name__ == "__main__":
#     md = Model()
#     md.download_model()
#     print(md.getModel())