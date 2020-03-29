from google_drive_downloader import GoogleDriveDownloader as gdd
import os
# https://drive.google.com/open?id=1PwifTMRZxzIbl-yDlR9cCVZrNxYg1JNd

class GoogleDriveModel():
    def __init__(self,file_id,model_name):
        """
            file_id{{string}}: unique ID alloted to file by google
            model_name{{string}}: name of the file in google drive (can be modified by user)
        """
        self.file_id  = file_id
        self.save_url = './'+str(model_name)
        """
            function is used to download weight file
        """
    def DownloadModel(self):
        try:
            if(os.path.exists(self.save_url)==False):
                gdd.download_file_from_google_drive(file_id=self.file_id,
                                            dest_path=self.save_url,
                                            unzip=True)
                print("Model downloaded")
            else:
                print("Model already present")
        except Exception as e:
            print("Caught Exception: "+str(e))
            
        """
            function is used to get path of saved model and if not present, return empty string
        """
    def getModel(self):
        try:
            if(os.path.exists(self.save_url)==True):
                path = os.path.abspath(self.save_url)
                return path
            else:
                print("Model not present")
                print("Download file first")
                return ""
        except Execption as e:
            print("Model not present")
            print("Download file first")
            return ""
			
#if __name__ == "__main__":
#     md = GoogleDriveModel("1PwifTMRZxzIbl-yDlR9cCVZrNxYg1JNd","weight.hdf5")
#     md.DownloadModel()
#     print(md.getModel())